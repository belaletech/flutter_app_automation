import os
from appium.webdriver import Remote
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.options.common import AppiumOptions  # Import AppiumOptions
from configs.config import APPIUM_SERVER, CAPS

# Convert CAPS dictionary into AppiumOptions
options = AppiumOptions()
options.load_capabilities(CAPS)

# Start Appium Driver with AppiumOptions
driver = Remote(command_executor=APPIUM_SERVER, options=options)  # Use options instead of CAPS
finder = FlutterFinder()

# Click on the number 2 using FlutterFinder
num2_finder = finder.by_value_key("2")  # Use `by_value_key` instead of XPath
num2_element = FlutterElement(driver, num2_finder)
num2_element.click()

# Click on the '+' button
plus_finder = finder.by_value_key("+")  
plus_element = FlutterElement(driver, plus_finder)
plus_element.click()

# Click on the number 3
num3_finder = finder.by_value_key("3")  
num3_element = FlutterElement(driver, num3_finder)
num3_element.click()

# Click on the '=' button to get the result
equals_finder = finder.by_value_key("=")  
equals_element = FlutterElement(driver, equals_finder)
equals_element.click()

# Get the result displayed on the calculator
result_finder = finder.by_value_key("result")  # Assuming your result element has a key like "result"
result_element = FlutterElement(driver, result_finder)
print("Calculation Result:", result_element.text)

# Quit driver after execution
driver.quit()
