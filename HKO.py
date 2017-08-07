import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class MyOb(unittest.TestCase):
    "Class to run tests against MyObservator app"

    def setUp(self):
        "Setup for the test"
        #the landing page of this test is agreement page
        desired_caps = {'platformName': 'Android', 'platformVersion': '5.0.1', 'deviceName': 'K01Q',
                        'appPackage': 'hko.MyObservatory_v1_0', 'appActivity': '.AgreementPage'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_HK_nine_days(self):
        "test start"
        agree_button = self.driver.find_element_by_id('hko.MyObservatory_v1_0:id/btn_agree')

        agree_button.click()

        agree_button.click()
        sleep(3)
        dismiss_button = self.driver.find_element_by_id('hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip')
        dismiss_button.click()
        sleep(5)

        side_menu = self.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Navigate up"]')
        side_menu.click()
        sleep(3)

        self.driver.swipe(100,930,100,600)
        sleep(5)
        action = TouchAction(self.driver)
        action.tap(x=150,y=730).perform()

        sleep(5)


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyOb)
    unittest.TextTestRunner(verbosity=2).run(suite)
