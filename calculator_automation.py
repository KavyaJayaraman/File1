from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time



class calculator:

    cap = {
    "appium:deviceName": "Samsung",
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.google.android.calculator",
    "appium:appActivity": "com.android.calculator2.Calculator"
    }

    def initiate_Driver(self):
        #self.apppium_service = AppiumService()
        #global appium_service
       
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error:Appium server not working ...")

    def calculator_addition(self):
        try:
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_3").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_5").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/clr").click()
            time.sleep(2)
            result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text

            if int(result)==8:
                print("the result is as expected as :"+ result)

        except:
            print("an error occured ")


    def calculator_subtraction(self):
        try:
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_8").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_sub").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2").click()
            time.sleep(2)
            driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()
            time.sleep(2)
            result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text

            if int(result)==6:
                print("the result is as expected as :"+ result)

        except:
            print("an error occured ")


    def close_driver(self):
        driver.quit()
        print("Driver instance closed successfully")
        time.sleep(20)

obj = calculator()
obj.initiate_Driver()
obj.calculator_addition()
obj.calculator_subtraction()
obj.close_driver()
