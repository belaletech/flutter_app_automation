import os

LT_USERNAME, LT_ACCESS_KEY = os.getenv("LT_CREDENTIALS").split(":")
APP_URL = os.getenv("LAMBDATEST_APP_URL")
LT_BUILD_NAME = os.getenv("BUILD_NUMBER")

assert LT_USERNAME and LT_ACCESS_KEY, "❌ LambdaTest credentials are missing"
assert APP_URL, "❌ LAMBDATEST_APP_URL is missing"

APPIUM_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"

CAPS = {
    "build": LT_BUILD_NAME or "Default Jenkins Build",
    "platformName": "Android",
    "automationName": "flutter",
    "platformVersion": "13",
    "deviceName": "Galaxy S23+",
    "app": APP_URL,
    "isRealMobile": True
}
