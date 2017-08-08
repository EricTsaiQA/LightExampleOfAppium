# MyObservatory

This is a test script to presnet automation test for Android application MyObservatory

# Environment ( this is the environment i run this script so it nice you can have similar things before you run it)
1. Macbook pro running on IOS 10.12.3
2. Appium v1.6.5
3. Python 3.6
4. Python package, Appium-Python-Client(0.24), pytest(3.2.0), selenium(3.4.3)
5. Android application MyObservatory, please download it from Google play store

# Must know
Please modify desired caps to fit your test device. 

my condig is:
platformVersion': '7.1.2', 'deviceName': 'Nexus 5X'

but you should modify above data in test script to fit your environment

# Usage
1. clone to local machine
2. start appium service
3. run  "python HKO.py"
4. check console log also status on device

# Known issue
Sometimes it fails when finding item "HK 9 Day forecast" in side menu. the script seems not did the "swipe" action on device
I haven't digged into why this happend.
The workaround is to kill and restart your appium service. Then run scritp agian.



