import time
import allure
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


desired_cap = {
        "appium:deviceName": "emulator-5556",
        "platformName": "Android",
        "appium:app": "C:\\Users\\godknows_velocityinc\\Downloads\\points.apk"
    }


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(300)
print("Device has been connected, Points Africa App is ready")
# Find the element by Accessibility ID and click it
element = driver.find_element(MobileBy.ACCESSIBILITY_ID, "Sign In")
element.click()
print("Click on Sign In button")

# Using X-Path method
# element = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Sign In"]')
# element.click()

pass_eye = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="+233"]/android.widget.ImageView[2]')

# Click the dropdown to open it
pass_eye.click()
print("show password")


# Function to scroll to the desired country
def test_scroll_to_country(chosen_nation):
    global dropdown_items  # Declare the variable as global to access and update it
    while True:
        for item in dropdown_items:
            if chosen_nation in item.get_attribute("content-desc"):
                return item
        # Perform a swipe action to scroll down the dropdown list
        height = driver.get_window_size()['height']
        width = driver.get_window_size()['width']
        driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2, duration=800)
        # Update the list of dropdown items after scrolling
        dropdown_items = driver.find_elements(MobileBy.XPATH, '//android.widget.ImageView[@content-desc]')


# Wait for the dropdown items to load
wait = WebDriverWait(driver, 10)
print("Scroll to find desired country , Zimbabwe in this case")

dropdown_items = wait.until(EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.ImageView['
                                                                                 '@content-desc]')))

# Scroll to the desired country (e.g., "Zimbabwe")
desired_country = "+263 Zimbabwe"
desired_country_element = test_scroll_to_country(desired_country)

if desired_country_element:
    # Perform a tap action to click the desired country element
    action = TouchAction(driver)
    action.tap(desired_country_element).perform()
else:
    print("Desired country not found in the dropdown.")

# It's a good practice to add some wait after interacting with the dropdown
# in case any animations or delays are present in the app.
driver.implicitly_wait(2)

phone_insert = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                    '.FrameLayout/android.widget.FrameLayout/android.view.View'
                                                    '/android.view.View/android.view.View/android.view.View/android'
                                                    '.view.View/android.view.View/android.widget.EditText[1]'))
)

# Use TouchAction to simulate a tap on the input field
TouchAction(driver).tap(phone_insert).perform()

phone_number = "782670023"
phone_insert.send_keys(phone_number)

# Hide the keyboard if needed
driver.hide_keyboard()

driver.implicitly_wait(2)

password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                    '.FrameLayout/android.widget.FrameLayout/android.view.View'
                                                    '/android.view.View/android.view.View/android.view.View/android'
                                                    '.view.View/android.view.View/android.widget.EditText[2]'))
)

# Use TouchAction to simulate a tap on the input field
TouchAction(driver).tap(password_input).perform()

pass_enter = "Godknows@100"
password_input.send_keys(pass_enter)

# Hide the keyboard if needed
driver.hide_keyboard()

# Show password eye

pass_eye = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                               '.FrameLayout/android.view.View/android.view.View/android.view.View'
                                               '/android.view.View/android.view.View/android.view.View/android.widget'
                                               '.EditText[2]/android.widget.ImageView')

# Click password eye to show
pass_eye.click()

driver.implicitly_wait(3)

pass_eye.click()

# Checkbox for remember me
remember_me_checkbox = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                           '.FrameLayout/android.widget.FrameLayout/android.view.View'
                                                           '/android.view.View/android.view.View/android.view.View'
                                                           '/android.view.View/android.view.View/android.widget'
                                                           '.ImageView[4]')

# Click on the checkbox to toggle its selection
remember_me_checkbox.click()

# Then sign in

sign_inn = driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="Sign In"])[2]')

# Click the dropdown to open it
sign_inn.click()

driver.implicitly_wait(10)
# clear the biometrics pop-up(Activate)
activate_btn = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Activate"]')
activate_btn.click()
time.sleep(5)

# scroll on all the deals
driver.implicitly_wait(10)
# Find the initial number of deals on the dashboard (optional, if you want to track when the list ends)
initial_deals_count = len(driver.find_elements(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                               '.LinearLayout/android.widget.FrameLayout/android'
                                                               '.widget.FrameLayout/android.widget.FrameLayout'
                                                               '/android.view.View/android.view.View/android.view'
                                                               '.View/android.view.View/android.widget.ScrollView'))
# Replace with the XPath to locate all deal elements

# Swipe and keep scrolling until the number of deals remains the same (indicating the end of the list)
while True:
    # Swipe from the bottom of the screen to the top
    height = driver.get_window_size()['height']
    width = driver.get_window_size()['width']
    driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2, duration=800)
    driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2, duration=800)

    # Wait for a short time to let the list load and settle after scrolling
    time.sleep(10)

    # Find the updated number of deals on the dashboard
    updated_deals_count = len(driver.find_elements(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android'
                                                                   '.widget.LinearLayout/android.widget.FrameLayout'
                                                                   '/android.widget.FrameLayout/android.widget'
                                                                   '.FrameLayout/android.view.View/android.view.View'
                                                                   '/android.view.View/android.view.View/android'
                                                                   '.widget.ScrollView'))

    # Check if the number of deals remains the same as the initial count
    if updated_deals_count == initial_deals_count:
        break  # Break the loop as you have reached the end of the list

    # Update the initial count for the next iteration
    initial_deals_count = updated_deals_count

    # Optional: Wait for a short time to let the scrolling action complete (if required)
    time.sleep(10)

# click on the Navigation Drawer
driver.implicitly_wait(20)
nav_drawer = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                 '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                 '.view.View/android.view.View/android.widget.ImageView[1]')
nav_drawer.click()

driver.implicitly_wait(10)
time.sleep(10)

edit_profile = driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Edit Profile')
edit_profile.click()
time.sleep(10)

# click on change image icon
driver.implicitly_wait(5)
change_image = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                   '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                   '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                   '.view.View/android.view.View/android.view.View/android.view.View'
                                                   '/android.widget.ImageView[3]')
change_image.click()
time.sleep(5)

driver.implicitly_wait(5)
choose_image = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                   '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                   '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                   '.view.View['
                                                   '1]/android.view.View/android.widget.ScrollView/android.view.View['
                                                   '2]/android.view.View/android.view.View/android.widget.ImageView[1]')
choose_image.click()
time.sleep(5)

save = driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.view.View/android.view.View/android.view.View/android.view.View'
                                           '/android.view.View/android.view.View/android.widget.ImageView[2]')
save.click()

time.sleep(5)

cancel_btn = driver.find_element(MobileBy.CLASS_NAME, "android.widget.Button")

cancel_btn.click()

# offers page
time.sleep(5)

offer_btn = driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Offers"]')

offer_btn.click()

# Rewards page
time.sleep(5)
offer_btn = driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Rewards"]')

offer_btn.click()

# Home page
time.sleep(2)
home_btn = driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Home"]')

home_btn.click()
