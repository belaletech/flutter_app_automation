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

print("✅ Appium session started successfully!")

# ✅ Click on "2"
num2_finder = finder.by_value_key("button_2")
num2_element = FlutterElement(driver, num2_finder)
num2_element.click()
print("✅ Clicked on 2")

# ✅ Click on "+"
plus_finder = finder.by_value_key("button_+")
plus_element = FlutterElement(driver, plus_finder)
plus_element.click()
print("✅ Clicked on +")

# ✅ Click on "3"
num3_finder = finder.by_value_key("button_3")
num3_element = FlutterElement(driver, num3_finder)
num3_element.click()
print("✅ Clicked on 3")

# ✅ Click on "="
equals_finder = finder.by_value_key("button_=")
equals_element = FlutterElement(driver, equals_finder)
equals_element.click()
print("✅ Clicked on =")

# ✅ Get the result displayed on the calculator
result_finder = finder.by_value_key("output_text")
result_element = FlutterElement(driver, result_finder)
result_text = result_element.text
print(f"✅ Calculation Result: {result_text}")
driver.quit()

print("✅ Appium session closed.")