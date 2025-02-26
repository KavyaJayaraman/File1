from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class saucelab:

    cap = {
    "appium:deviceName": "Samsung",
    "appium:platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:app": "C:\\Users\\2022368\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
    "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity"
    }

    def scroll(self):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(619, 2021)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(667, 787)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def initiate_Driver(self):
        #self.apppium_service = AppiumService()
        #global appium_service
       
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error:Appium server not working ...")

    def launch_saucelab(self):
        try:
            driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='test-Username']").send_keys("standard_user")
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='test-Password']").send_keys("secret_sauce")
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-LOGIN']").click()
            time.sleep(2)
        except:
            print("not as expected")

    def add_to_cart(self):
            
            count = len(driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='test-Item title']"))
            for i in range(1,count+1):
                item = driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]").text
                print(item)

            driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]").click()
            time.sleep(3)
            driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-ADD TO CART']").click()
            time.sleep(3)

    def validate_cart(self):
            driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView").click()
            time.sleep(2)
            cart_count = len(driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-REMOVE']"))
            print("item in cart is :",cart_count)

            driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView").click()
            time.sleep(3)

    

    def validate_checkout(self):
            
            self.scroll()
            el1 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CHECKOUT\")")
            el1.click()
            time.sleep(2)
            el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-First Name")
            el2.send_keys("abc")
            time.sleep(2)
            el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Last Name")
            el3.send_keys("xyz")
            time.sleep(2)
            el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
            el4.send_keys("123456")
            time.sleep(2)
            el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CONTINUE")
            el5.click()
            time.sleep(2)
            self.scroll()
            time.sleep(2)

            el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-FINISH")
            el6.click()
            time.sleep(2)

    def close_driver(self):
        driver.quit()
        print("Driver instance closed successfully")
        time.sleep(5)

obj = saucelab()
obj.initiate_Driver()
obj.launch_saucelab()
obj.add_to_cart()
obj.validate_cart()
obj.validate_checkout()
obj.close_driver()