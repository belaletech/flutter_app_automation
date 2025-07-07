import os

LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")
APP_ID = os.getenv("LAMBDATEST_APP_URL")

APPIUM_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"

CAPS = {
    "build": "Python Appium Calculator Test",
    "platformName": "Android",
    "automationName": "flutter",
    "platformVersion": "13",
    "deviceName": "Galaxy S23+",
    "app": APP_ID,
    "isRealMobile": True
}
