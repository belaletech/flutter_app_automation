import os
from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from configs.config import APPIUM_SERVER, CAPS

# Start Appium Driver
driver = Remote(APPIUM_SERVER, CAPS)
finder = FlutterFinder()

# Click on the number 2
num2_finder = driver.find_element("xpath", "//*[@content-desc='2']")
num2_finder.click()

# Click on the '+' button
plus_finder = driver.find_element("xpath", "//*[@content-desc='+']")
plus_finder.click()

# Click on the number 3
num3_finder = driver.find_element("xpath", "//*[@content-desc='3']")
num3_finder.click()

# Click on the '=' button to get the result
equals_finder = driver.find_element("xpath", "//*[@content-desc='=']")
equals_finder.click()

# Get the result displayed on the calculator
result_finder = driver.find_element("xpath", "//*[@class='android.widget.TextView']")
print("Calculation Result:", result_finder.text)

# Quit driver after execution
driver.quit()
