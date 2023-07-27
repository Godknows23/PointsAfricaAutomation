
import click as click
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap= {
    "appium:deviceName": "emulator-5556",
    "platformName": "Android",
    "appium:app": "C:\\Users\\godknows_velocityinc\\Downloads\\app.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(300)
# Find the element by Accessibilty ID and click it
element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Sign In")
element.click()
# Using X-Path method
# element = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Sign In"]')
# element.click()

dropdown = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="+233"]/android.widget.ImageView[2]')

# Click the dropdown to open it
dropdown.click()
# Function to scroll to the desired country
def scroll_to_country(desired_country):
    global dropdown_items  # Declare the variable as global to access and update it
    while True:
        for item in dropdown_items:
            if desired_country in item.get_attribute("content-desc"):
                return item
        # Perform a swipe action to scroll down the dropdown list
        height = driver.get_window_size()['height']
        width = driver.get_window_size()['width']
        driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2, duration=800)
        # Update the list of dropdown items after scrolling
        dropdown_items = driver.find_elements(MobileBy.XPATH, '//android.widget.ImageView[@content-desc]')

# Wait for the dropdown items to load
wait = WebDriverWait(driver, 10)
dropdown_items = wait.until(EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.ImageView[@content-desc]')))

# Scroll to the desired country (e.g., "Zimbabwe")
desired_country = "+263 Zimbabwe"
desired_country_element = scroll_to_country(desired_country)

if desired_country_element:
    # Perform a tap action to click the desired country element
    action = TouchAction(driver)
    action.tap(desired_country_element).perform()
else:
    print("Desired country not found in the dropdown.")

# It's a good practice to add some wait after interacting with the dropdown
# in case any animations or delays are present in the app.
driver.implicitly_wait(2)



phone_number_input_locator = (MobileBy.ACCESSIBILITY_ID, "signInTextField1")

phone_number_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(phone_number_input_locator)
)

# Use TouchAction to simulate a tap on the phone number input field
TouchAction(driver).tap(phone_number_input).perform()

# Now you can proceed to send the phone number
phone_number = "782670023"
phone_number_input.send_keys(phone_number)

# Hide the keyboard if needed
driver.hide_keyboard()



# Optional: Wait for a short time to let the password input be processed
driver.implicitly_wait(3)

password_field = driver.find_element(MobileBy.ACCESSIBILITY_ID, "passwordSignInTextField")

# Click on the password field to activate it
password_field.click()

# Input the password "Godknows@25" using driver.send_keys()
password = "Godknows"
password_field.send_keys(password)

# Optional: Wait for a short time to let the password input be processed

driver.implicitly_wait(3)






