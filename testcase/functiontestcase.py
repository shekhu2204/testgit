import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#from selenium.webdriver import ActionChains
#from selenium.webdriver.common.actions import interaction
#from selenium.webdriver.common.actions.action_builder import ActionBuilder
#from selenium.webdriver.common.actions.pointer_input import PointerInput

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

    el3 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/btnLogin")
    el3.click()

    time.sleep(10)

def test_Orderlist():
    el4 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/text_order")
    el4.click()
    time.sleep(5)

def test_Wallets():
    el5 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/offers")
    el5.click()
    time.sleep(5)

def test_WatllHistry():
    el6 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/image")
    el6.click()
    time.sleep(5)


def test_rcharge():
    el7 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvRecharge")
    el7.click()

    time.sleep(5)

    el8 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/etRechargeAmount")
    el8.send_keys("100")

    time.sleep(10)
    el9 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/btnRecharge")
    el9.click()

    time.sleep(10)

def test_myProfile():
    el10 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/profile")
    el10.click()

    time.sleep(5)


def test_prfilMyWallet():
    el11 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvWallet")
    el11.click()

    time.sleep(5)

    el12 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/back")
    el12.click()
    time.sleep(5)

def test_privact():
    el13 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/profile")
    el13.click()
    time.sleep(5)
    el14 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvPrivacy")
    el14.click()

    time.sleep(10)

    el15 = webdriver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
    el15.click()

    time.sleep(15)
    webdriver.back()

def test_AboutUs():
    el16 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvAbout")
    el16.click()
    time.sleep(5)
    el17 = webdriver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView")
    el17.click()
    time.sleep(15)
    webdriver.back()

    time.sleep(5)

def test_Termscondition():

    el18 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvTnC")
    el18.click()
    time.sleep(5)
    el19 = webdriver.find_element(by=AppiumBy.XPATH,  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
    el19.click()
    time.sleep(15)
    webdriver.back()

def test_RefundCancellation():
    el20 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvRefundsContactUs")
    el20.click()
    time.sleep(5)
    el20 = webdriver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
    el20.click()
    time.sleep(15)
    webdriver.back()


def test_PrivacyPolicy():
    el21 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvPrivacy")
    el21.click()
    time.sleep(5)

    el22 = webdriver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
    el22.click()
    time.sleep(15)
    webdriver.back()


def test_ContactUS():
    el23 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvContactUs")
    el23.click()
    time.sleep(5)
    el24 = webdriver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
    el24.click()
    time.sleep(15)

    webdriver.back()

def test_Feedback():
    el25 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvFeedback")
    el25.click()
    time.sleep(5)
    el26 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/back")
    el26.click()

def test_Home():
    el27 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/home")
    el27.click()

def test_Logout():
    el41 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/profile")
    el41.click()
    time.sleep(5)
    el42 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/tvLogout")
    el42.click()
    time.sleep(5)
    el43 = webdriver.find_element(by=AppiumBy.ID, value="uvm.com.snackit_vend:id/btnYesPopup")
    el43.click()
