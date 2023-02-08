from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def test_login():
 desired_cap = {
    "platformName": "android",
    "deviceName": "a4ad90d8",
    "app": "/Users/Lenovo/Downloads/oselVend08082022.apk/",
    "appPackage": "uvm.com.snackit_vend",
    "appWaitActivity": "uvm.com.snackit_vend.FragmentActivity.Login",
    "newCommandTimeout": "60",
    "noReset": "true"

}

webdriver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

# .......................login page automation..............#

webdriver.implicitly_wait(5)

el1 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/etUserName")
el1.click()
el1.send_keys("C.shekhar1@limitlessmobil.com")
webdriver.back()
el2 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/etPassword")
el2.click()
el2.send_keys("Negi@123")
webdriver.back()


el3 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/btnLogin")
el3.click()
