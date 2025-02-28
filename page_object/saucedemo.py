from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def scroll(driver):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(619, 2021)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(667, 787)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

def username():
        return "//android.widget.EditText[@content-desc='test-Username']"
def password():
        return "//android.widget.EditText[@content-desc='test-Password']"
def login():
        return "//android.view.ViewGroup[@content-desc='test-LOGIN']"

def list_pdt():
        return "//android.view.ViewGroup[@content-desc='test-Toggle']/android.widget.ImageView"
def pdt_filter():
        return "//android.view.ViewGroup[@content-desc='test-Modal Selector Button']/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"
def low_high():
        return "new UiSelector().text(\"Price (low to high)\")"
def first_item():
        return "//android.widget.TextView[@content-desc='test-Price' and @text='$7.99']"
def second_item():
        return "//android.widget.TextView[@content-desc='test-Price' and @text='$9.99']"

def high_low():
        return "new UiSelector().text(\"Price (high to low)\")"
def third_item():
        return "//android.widget.TextView[@content-desc='test-Price' and @text='$49.99']"
def fourth_item():
        return "//android.widget.TextView[@content-desc='test-Price' and @text='$29.99']"

def itemCount():
        return "//android.widget.TextView[@content-desc='test-Item title']"
def printItem(i):
        return "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]"
def cart():
        return  "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
def remove():
        return "//android.view.ViewGroup[@content-desc='test-REMOVE']"
def checkout():
        return "new UiSelector().text(\"CHECKOUT\")"
def firstname():
        return "test-First Name"
def lastname():
        return "test-Last Name"
def zip():
        return "test-Zip/Postal Code"
def cont():
        return "test-CONTINUE"
def finish():
        return "test-FINISH"
