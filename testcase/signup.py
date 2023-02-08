from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
  "platformName": "android",
  "deviceName": "a4ad90d8",
  "app": "/Users/Lenovo/Downloads/oselVend08082022.apk/",
  "appPackage" : "uvm.com.snackit_vend",
  "appWaitActivity" :"uvm.com.snackit_vend.FragmentActivity.Login"

   }

webdriver = webdriver.Remote( "http://localhost:4723/wd/hub",desired_cap)

webdriver.implicitly_wait(5)

def test_Signup():
    el1 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/signUp")
    el1.click()
el2 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/input_name")
el2.click()
el2.send_keys("CSN")
webdriver.back()
el3 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/input_email")
el3.click()
el3.send_keys("CSN@gmail.com")
webdriver.back()
el4 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/input_password")
el4.click()
el4.send_keys("123456")
webdriver.back()
el5 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/input_ConfirmPassword")
el5.click()
el5.send_keys("123456")
webdriver.back()
el6 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvPhone")
el6.click()
el6.send_keys("8447123255")
webdriver.back()

el7 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/ivMale")
el7.click()
el8 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/btnSignUp")
el8.click()

el3 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/btnYesPopup")
el3.click()

webdriver.implicitly_wait(5)
