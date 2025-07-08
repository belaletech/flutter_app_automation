import os

LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")
APP_URL = os.getenv("LAMBDATEST_APP_URL")

# Validate required env vars
assert LT_USERNAME and LT_ACCESS_KEY, "❌ LambdaTest credentials are missing"
assert APP_URL, "❌ LAMBDATEST_APP_URL is missing"

APPIUM_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"

CAPS = {
    "build": "Python Appium Calculator Test",
    "platformName": "Android",
    "automationName": "flutter",
    "platformVersion": "13",
    "deviceName": "Galaxy S23+",
    "app": APP_URL,
    "isRealMobile": True
}
