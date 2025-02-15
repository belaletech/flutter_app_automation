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

# ✅ Get and Verify the Addition Result
result_finder = finder.by_value_key("output_text")
result_element = FlutterElement(driver, result_finder)
result_text = result_element.text
print(f"✅ Addition Result: {result_text}")

# ✅ Click on "C" to Clear the Calculator
clear_finder = finder.by_value_key("button_C")  # Use valueKey if available
clear_element = FlutterElement(driver, clear_finder)
clear_element.click()
print("✅ Clicked on Clear")

# ✅ Now Proceed to Multiplication
num6_finder = finder.by_value_key("button_6")
num6_element = FlutterElement(driver, num6_finder)
num6_element.click()
print("✅ Clicked on 6")

mult_finder = finder.by_value_key("button_*")  # Ensure correct key
mult_element = FlutterElement(driver, mult_finder)
mult_element.click()
print("✅ Clicked on *")

num7_finder = finder.by_value_key("button_7")
num7_element = FlutterElement(driver, num7_finder)
num7_element.click()
print("✅ Clicked on 7")

equals_finder = finder.by_value_key("button_=")
equals_element = FlutterElement(driver, equals_finder)
equals_element.click()
print("✅ Clicked on =")

# ✅ Get Final Multiplication Result
final_result_finder = finder.by_value_key("output_text")
final_result_element = FlutterElement(driver, final_result_finder)
final_result_text = final_result_element.text
print(f"✅ Multiplication Result: {final_result_text}")

driver.quit()
print("✅ Appium session closed.")
