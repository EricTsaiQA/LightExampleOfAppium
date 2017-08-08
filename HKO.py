import sys
import logging
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

logging.basicConfig(stream=sys.stdout,level=logging.INFO)

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
        logging.info('start to print test step log below')
        logging.info('Press OK button to pass landing page')
        sleep(2)
        agree_button = self.driver.find_element_by_id('hko.MyObservatory_v1_0:id/btn_agree')
        agree_button.click()
        agree_button.click()

        logging.info('Press allow button to pass location serveir permission page')
        sleep(2)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        logging.info('Dismiss whats new page')
        sleep(2)
        self.driver.find_element_by_id('hko.MyObservatory_v1_0:id/btn_friendly_reminder_skip').click()

        sleep(3)

        # Get window size, width and height will be used to perform tap side menu action
        screen_size = self.driver.get_window_size()
        max_width = screen_size["width"]
        max_height = screen_size["height"]
        logging.info('Measure window size and tap corner to open side menu')
        sleep(2)
        action = TouchAction(self.driver)
        action.tap(x=(max_width * 0.06), y=(max_height * 0.08)).perform()

        logging.info('Browse menu')
        sleep(2)
        el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Storm Track")')
        el2 = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Weather video")')
        action.press(el1).move_to(el2).release().perform()

        sleep(2)
        # Verification - check we can select HK 9 day forecast from side menu, show msg when failed
        logging.info('Find and tap HK 9-Day Forecast in menu')
        self.assertTrue(self.driver.find_element_by_android_uiautomator('new UiSelector().text("HK 9-Day Forecast")'),
                        msg="Fail to get HK 9day forecast button in menu")
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("HK 9-Day Forecast")').click()
        sleep(2)

        logging.info('Open HK 9-Day Forecast page')
        # Verification - make sure we are in HK 9 day forecast page by title, show msg when failed
        self.assertTrue(self.driver.find_element_by_android_uiautomator('new UiSelector().text("HK 9-Day Forecast")'),
                        msg="HK 9-day forecast page is not opened")

        # Browse page and collect forecast date to a list, eventually we should have 9 days forecast on this page
        forecast_raw = []
        detect_to_bottom = "null"
        forecast_date = []

        while True:
            logging.info('Browsing and try to find 9 days forecast on page')
            sleep(1)
            forecast_raw.extend(self.driver.find_elements_by_id('hko.MyObservatory_v1_0:id/sevenday_forecast_date'))

            for i in range(len(forecast_raw)):
                forecast_date.append(forecast_raw[i].__getattribute__('text'))

            if detect_to_bottom == forecast_date[-1]:
                break

            detect_to_bottom = forecast_date[-1]
            action.press(x=(max_width * 0.5), y=(max_height * 0.9)).move_to(x=0, y=-(max_height * 0.3)).perform()
            forecast_raw = []
            sleep(2)

        # Verification - make sure there are 9 days forecast show on page, show msg when failed
        self.assertEqual(len(list(set(forecast_date))), 9, msg="HK 9 days forecast display problem, please check")

        logging.info('Test is completed')
        sleep(3)
        self.driver.close_app()

#
#
# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyOb)
    unittest.TextTestRunner(verbosity=2).run(suite)
