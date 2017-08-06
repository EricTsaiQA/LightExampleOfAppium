import os
import unittest
from appium import webdriver
from time import sleep


class MyOb(unittest.TestCase):
    "Class to run tests against MyObservator app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = 'K01Q'
        desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
        desired_caps['appActivity'] = '.AgreementPage'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_launch_app(self):
        "launch and wait 5 seconds"
        sleep(5)

    def test_nine_days(self):
        self.driver.get_screenshot_as_file('test.png')
        self.driver.close_app()


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyOb)
    unittest.TextTestRunner(verbosity=2).run(suite)
