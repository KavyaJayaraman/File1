from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
file_html = open("C:\\Users\\2022368\\Documents\\automation\\alllinks.html","w")
 
tableHeader = '''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <style>
        table, th, td {
        border:1px solid black;
        }
        </style>
        <body>
        <table>
    <tr>
        <th>Sl.No</th>
        <th>Link Name</th>
        <th>LInk href Value</th>
    </tr>
'''
 
 
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.zomato.com/")
count = len(driver.find_elements(By.XPATH, "//a"))
 
htmlBody = ""
 
for a in range(1, count + 1):
    hrefValue = driver.find_element(By.XPATH, "(//a)[" + str(a) + "]").get_attribute("href")
    linkName = driver.find_element(By.XPATH, "(//a)[" + str(a) + "]").text
    print(linkName)
    print(hrefValue)    
 
    data = "<tr><th>"+str(a)+"</th><th>"+str(linkName)+"</th><th>"+str(hrefValue)+"</th></tr>"
    htmlBody = htmlBody+data
 
driver.implicitly_wait(10)
driver.quit()
 
tableFooter = '''
            </table>
            </body>
            </html>
'''
 
#write the html
file_html.write(tableHeader+htmlBody+tableFooter)
 
#saving data into html file
file_html.close()
 
 