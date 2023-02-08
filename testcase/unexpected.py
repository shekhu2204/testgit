import time
#import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


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

webdriver.wait_activity('com.ali.user.mobile.login.ui.UserLoginActivity', 1)


