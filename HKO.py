import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class MyOb(unittest.TestCase):
    "Class to run tests against MyObservator app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {'platformName': 'Android', 'platformVersion': '7.1.2', 'deviceName': 'Nexus 5X',
                        'appPackage': 'hko.MyObservatory_v1_0', 'appActivity': '.AgreementPage'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_HK_nine_days(self):
        "Test case: open HK 9 days forecast"
        agree_button = self.driver.find_element_by_id('hko.MyObservatory_v1_0:id/btn_agree')
        agree_button.click()
        agree_button.click()

        sleep(1)

        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        self.driver.find_element_by_id('hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip').click()

        sleep(3)

        screen_size = self.driver.get_window_size()
        max_width = screen_size["width"]
        max_height = screen_size["height"]

        action = TouchAction(self.driver)
        action.tap(x=(max_width*0.06),y=(max_height*0.08)).perform()
        #self.driver.find_element_by_android_uiautomator('new UiSelector().description("Navigate up")').click()
        #Having problem to find side menu and i did not figure out why
        #therefore i specified x,y positon to tap
        sleep(2)
        #scroll and tap HK 9-days forecast
        el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Storm Track")')
        el2 = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Weather video")')
        action.press(el1).move_to(el2).release().perform()
        sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("HK 9-Day Forecast")').click()
        sleep(2)

        try:
            el3 = self.driver.find_element_by_android_uiautomator('new UiSelector().text("8 Aug")')
        except:
            raise Exception('display problem in HK 9-Day forecast, please check 1')

        action.press(x=(max_width*0.5),y=(max_height*0.9)).move_to(x=0,y=-(max_height*0.5)).release().perform()

        try:
            el4 = self.driver.find_element_by_android_uiautomator('new UiSelector().text("16 Aug")')
        except:
            raise Exception('display problem in HK 9-Day forecast, please check 2')

        sleep(2)

        #self.assertTrue(self.driver.find_element_by_android_uiautomator('new UiSelector().text("HK 9-Day Forecast")'),msg="HK 9-day forecast page is not opened")
        sleep(5)
        self.driver.close_app() # return to device home

#
#
# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyOb)
    unittest.TextTestRunner(verbosity=2).run(suite)
