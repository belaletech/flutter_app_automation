import os

# Retrieve credentials from environment variables
LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

APPIUM_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"

CAPS = {
    "build": "Python Appium Calculator Test",
    "platformName": "Android",
    "automationName": "flutter",
    "platformVersion": "13",
    "deviceName": "Galaxy S23+",
    "app": "lt://APP1016045521739462030652329",
    "isRealMobile": True
}
