from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
import pytest
from page_object import saucedemo



@pytest.mark.usefixtures("launch_app")
class Test_saucelab:

    
    def test_launch_saucelab(self,read_json):
        try:
            self.driver.find_element(AppiumBy.XPATH, saucedemo.username()).send_keys(read_json["username"])
            time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH, saucedemo.password()).send_keys(read_json["password"])
            time.sleep(2)
            self.driver.find_element(AppiumBy.XPATH, saucedemo.login()).click()
            time.sleep(2)
        except:
            print("not as expected")

    def test_add_to_cart(self):
            
            count = len(self.driver.find_elements(AppiumBy.XPATH, saucedemo.itemCount()))
            for i in range(1,count+1):
                item = self.driver.find_element(AppiumBy.XPATH,saucedemo.printItem(i) ).text
                print(item)

            self.driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]").click()
            time.sleep(3)
            self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-ADD TO CART']").click()
            time.sleep(3)

    def test_validate_cart(self):
            self.driver.find_element(AppiumBy.XPATH,saucedemo.cart()).click()
            time.sleep(2)
            cart_count = len(self.driver.find_elements(AppiumBy.XPATH, saucedemo.remove()))
            print("item in cart is :",cart_count)

            self.driver.find_element(AppiumBy.XPATH, saucedemo.cart()).click()
            time.sleep(3)

    

    def test_validate_checkout(self,read_json):
            
            saucedemo.scroll(self.driver)
            el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=saucedemo.checkout())
            el1.click()
            time.sleep(2)
            el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucedemo.firstname())
            el2.send_keys(read_json["firstname"])
            time.sleep(2)
            el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucedemo.lastname())
            el3.send_keys(read_json["lastname"])
            time.sleep(2)
            el4 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucedemo.zip())
            el4.send_keys(read_json["pin"])
            time.sleep(2)

            
            el5 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucedemo.cont())
            el5.click()
            time.sleep(2)
           
            saucedemo.scroll(self.driver)
            el6 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=saucedemo.finish())
            el6.click()
            time.sleep(2)

    

