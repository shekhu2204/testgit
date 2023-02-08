import time
import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput




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


def test_LOGIN():
    el1 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/etUserName")
    el1.click()
    el1.send_keys("C.shekhar1@limitlessmobil.com")
    webdriver.back()
    el2 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/etPassword")
    el2.click()
    el2.send_keys("Negi@123")
    webdriver.back()

    # webdriver.wait_activity('com.ali.user.mobile.login.ui.UserLoginActivity', 2)

    el3 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/btnLogin")
    el3.click()

    time.sleep(10)


def test_SELECT_product():

    el1 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/purchase_again")
    el1.click()
    time.sleep(3)

    actions = ActionChains(webdriver)
    actions.w3c_actions = ActionBuilder(webdriver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(79, 1590)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(75, 686)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    time.sleep(2)

    actions = ActionChains(webdriver)
    actions.w3c_actions = ActionBuilder(webdriver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(53, 1414)

    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(83, 979)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    time.sleep(2)

    el3 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/plus_quantity")
    el3.click()




def test_Vend_conti():

    e14 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/continue_")
    e14.click()
    time.sleep(3)

    el5 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/continue_layout")
    el5.click()
    time.sleep(5)


def test_vend_Later():
    el5 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/vend_later_icon")
    el5.click()
    time.sleep(2)

    el6 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/continue_")
    el6.click()
    time.sleep(5)

def test_select_payemnt():
    el9 = webdriver.find_element(AppiumBy.ID, value="uvm.com.snackit_vend:id/other_payment")
    el9.click()

    time.sleep(5)




