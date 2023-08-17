import time
import unittest
import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dropdown_items = []


@allure.story("Test Automation - Points Africa")
@allure.feature("Test - Open the Points Africa app and sign in")
@allure.testcase("Sign in")
class PointsAfrica(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with allure.step("Launch the Points Africa App"):
            desired_cap = {
                "appium:deviceName": "emulator-5556",
                "platformName": "Android",
                "appium:app": "C:\\Users\\godknows_velocityinc\\Downloads\\PointsAfricaProd.apk"
            }

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        cls.driver.implicitly_wait(300)

    @classmethod
    def tearDownClass(cls):
        try:
            print("Device has been connected, Points Africa App is ready")
            # Add any additional cleanup code here if needed
        finally:
            cls.driver.quit()

    def setUp(self):
        # Add any setup code specific to each test method here
        pass

    def tearDown(self):
        # Add any cleanup code specific to each test method here
        pass

    @allure.step("Click on Sign In button")
    def test_01_sign_in_and_transact(self):
        # Find the element by Accessibility ID and click it
        element = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Sign In")
        element.click()
        print("Click on Sign In button")

        # Using X-Path method
        # element = driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Sign In"]')
        # element.click()

        country_drop = self.driver.find_element(MobileBy.XPATH,
                                                '//android.view.View[@content-desc="+233"]/android.widget.ImageView[2]')

        # Click the dropdown to open it
        country_drop.click()
        print("Click the dropdown")

    @allure.step("Scroll to find Country")
    def zim_country(self, chosen_nation):
        while True:

            for item in self.dropdown_items:
                if chosen_nation in item.get_attribute("content-desc"):
                    return item
            # Perform a swipe action to scroll down the dropdown list
            height = self.driver.get_window_size()['height']
            width = self.driver.get_window_size()['width']
            self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                              duration=800)
            # Update the list of dropdown items after scrolling
            self.dropdown_items = self.driver.find_elements(MobileBy.XPATH,
                                                            '//android.widget.ImageView[@content-desc]')

    @allure.step("Select Zimbabwe")
    def test_02_country_selection(self):
        # Wait for the dropdown items to load
        wait = WebDriverWait(self.driver, 10)
        print("Scroll to find desired country , Zimbabwe in this case")

        self.dropdown_items = wait.until(
            EC.presence_of_all_elements_located((MobileBy.XPATH, '//android.widget.ImageView[@content-desc]')))

        # Scroll to the desired country (e.g., "Zimbabwe")
        desired_country = "+263 Zimbabwe"
        desired_country_element = self.zim_country(desired_country)

        if desired_country_element:
            # Perform a tap action to click the desired country element
            action = TouchAction(self.driver)
            action.tap(desired_country_element).perform()
        else:
            print("Desired country not found in the dropdown.")

        # It's a good practice to add some wait after interacting with the dropdown
        # in case any animations or delays are present in the app.
        self.driver.implicitly_wait(3)

    @allure.step("Enter Phone Number")
    def test_03_phone_number(self):
        phone_insert = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.widget.FrameLayout/android.view.View'
                                                            '/android.view.View/android.view.View/android.view.View'
                                                            '/android'
                                                            '.view.View/android.view.View/android.widget.EditText[1]'))
        )

        # Use TouchAction to simulate a tap on the input field
        TouchAction(self.driver).tap(phone_insert).perform()

        phone_number = "782670023"
        phone_insert.send_keys(phone_number)

        # Hide the keyboard if needed
        self.driver.hide_keyboard()

        self.driver.implicitly_wait(3)

    @allure.step("Enter your Password")
    def test_04_EnterPassword(self):
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.widget.FrameLayout/android.view.View'
                                                            '/android.view.View/android.view.View/android.view.View'
                                                            '/android'
                                                            '.view.View/android.view.View/android.widget.EditText[2]'))
        )

        # Use TouchAction to simulate a tap on the input field
        TouchAction(self.driver).tap(password_input).perform()

        pass_enter = "Godknows@25"
        password_input.send_keys(pass_enter)

        # Hide the keyboard if needed
        self.driver.hide_keyboard()

    @allure.step("Click on the Password")
    def test_05_PassEye(self):
        # Show password eye

        pass_eye = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout'
                                                            '/android.widget.FrameLayout/android.widget.FrameLayout'
                                                            '/android.widget'
                                                            '.FrameLayout/android.view.View/android.view.View/android'
                                                            '.view'
                                                            '.View'
                                                            '/android.view.View/android.view.View/android.view.View'
                                                            '/android.widget'
                                                            '.EditText[2]/android.widget.ImageView')

        # Click password eye to show
        pass_eye.click()

        self.driver.implicitly_wait(4)

        pass_eye.click()

    @allure.step("Remember Me")
    def test_06_RememberMe(self):
        # Checkbox for remember me
        remember_me_checkbox = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout'
                                                                        '/android.widget'
                                                                        '.LinearLayout/android.widget.FrameLayout'
                                                                        '/android'
                                                                        '.widget'
                                                                        '.FrameLayout/android.widget.FrameLayout'
                                                                        '/android'
                                                                        '.view.View'
                                                                        '/android.view.View/android.view.View/android'
                                                                        '.view.View'
                                                                        '/android.view.View/android.view.View/android'
                                                                        '.widget'
                                                                        '.ImageView[4]')

        # Click on the checkbox to toggle its selection
        remember_me_checkbox.click()

    @allure.step("Click sign In to proceed")
    def test_07_SignIn(self):
        # Then sign in

        sign_inn = self.driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="Sign In"])[2]')

        # Click the dropdown to open it
        sign_inn.click()

        self.driver.implicitly_wait(10)

    @allure.step("Activate Biometrics")
    def test_08_BiometricsActive(self):
        # clear the biometrics pop-up(Activate)
        activate_btn = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Activate"]')
        activate_btn.click()
        self.driver.implicitly_wait(10)

    @allure.step("Scroll on deals")
    def test_09_DealScroll(self):
        # scroll on all the deals
        self.driver.implicitly_wait(10)
        # Find the initial number of deals on the dashboard (optional, if you want to track when the list ends)
        initial_deals_count = len(self.driver.find_elements(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout'
                                                                            '/android.widget'
                                                                            '.LinearLayout/android.widget.FrameLayout'
                                                                            '/android'
                                                                            '.widget.FrameLayout/android.widget'
                                                                            '.FrameLayout'
                                                                            '/android.view.View/android.view.View'
                                                                            '/android.view'
                                                                            '.View/android.view.View/android.widget'
                                                                            '.ScrollView'))
        # Replace with the XPath to locate all deal elements

        # Swipe and keep scrolling until the number of deals remains the same (indicating the end of the list)
        while True:
            # Swipe from the bottom of the screen to the top
            height = self.driver.get_window_size()['height']
            width = self.driver.get_window_size()['width']
            self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                              duration=800)
            self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                              duration=800)

            # Wait for a short time to let the list load and settle after scrolling
            self.driver.implicitly_wait(10)

            # Find the updated number of deals on the dashboard
            updated_deals_count = len(self.driver.find_elements(MobileBy.XPATH, '/hierarchy/android.widget'
                                                                                '.FrameLayout/android'
                                                                                '.widget.LinearLayout/android.widget'
                                                                                '.FrameLayout'
                                                                                '/android.widget.FrameLayout/android'
                                                                                '.widget'
                                                                                '.FrameLayout/android.view.View/android'
                                                                                '.view.View'
                                                                                '/android.view.View/android.view.View'
                                                                                '/android'
                                                                                '.widget.ScrollView'))

            # Check if the number of deals remains the same as the initial count
            if updated_deals_count == initial_deals_count:
                break  # Break the loop as you have reached the end of the list

            # Update the initial count for the next iteration
            initial_deals_count = updated_deals_count

            # Optional: Wait for a short time to let the scrolling action complete (if required)
            self.driver.implicitly_wait(5)

    @allure.step("Click on the Navigation drawer")
    def test_10_NavDrawer(self):

        # click on the Navigation Drawer
        self.driver.implicitly_wait(10)
        nav_drawer = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                              '.LinearLayout'
                                                              '/android.widget.FrameLayout/android.widget.FrameLayout'
                                                              '/android'
                                                              '.widget.FrameLayout/android.view.View/android.view.View'
                                                              '/android'
                                                              '.view.View/android.view.View/android'
                                                              '.widget.ImageView[1]')
        nav_drawer.click()

        self.driver.implicitly_wait(5)
        time.sleep(5)

    @allure.step("Edit Profile Button")
    def test_11_EditProfile(self):

        edit_profile = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Edit Profile')
        edit_profile.click()
        time.sleep(5)

        # click on change image icon
        self.driver.implicitly_wait(5)

    @allure.step("Change Profile")
    def test_12_ChangeAvatar(self):

        change_image = self.driver.find_element(MobileBy.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                '.view.View/android.view.View/android.view.View/android.view.View'
                                                '/android.widget.ImageView[3]')
        change_image.click()
        time.sleep(5)

        self.driver.implicitly_wait(5)
        choose_image = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                                '.LinearLayout'
                                                                '/android.widget.FrameLayout/android.widget.FrameLayout'
                                                                '/android'
                                                                '.widget.FrameLayout/android.view.View/android.view'
                                                                '.View'
                                                                '/android'
                                                                '.view.View['
                                                                '1]/android.view.View/android.widget.ScrollView/android'
                                                                '.view.View['
                                                                '2]/android.view.View/android.view.View/android.widget'
                                                                '.ImageView[1]')
        choose_image.click()
        time.sleep(5)

        save = self.driver.find_element(MobileBy.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                        '/android.view.View/android.view.View/android.view.View/android.view.View'
                                        '/android.view.View/android.view.View/android.widget.ImageView[2]')
        save.click()

        time.sleep(5)

    @allure.step("Change Profile")
    def test_13_CancelBtn(self):
        cancel_btn = self.driver.find_element(MobileBy.CLASS_NAME, "android.widget.Button")
        cancel_btn.click()

    @allure.step("Click on Offers")
    def test_14_OffersBtn(self):
        # offers page
        time.sleep(5)
        offer_btn = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Offers"]')
        offer_btn.click()
        time.sleep(5)

    @allure.step("Click on Rewards")
    def test_15_RewardsBtn(self):
        # Rewards page
        time.sleep(5)
        offer_btn = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Rewards"]')

        offer_btn.click()

    @allure.step("Click on Favourites")
    def test_16_FavouritesBtn(self):
        # Favourites button
        time.sleep(5)
        fav_btn = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Favourites"]')

        fav_btn.click()
        self.driver.implicitly_wait(3)
        wait = WebDriverWait(self.driver, 3)
        offers_btn = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Offers"]')
        offers_btn.click()
        time.sleep(5)
        rewards_btn = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Rewards"]')
        rewards_btn.click()
        time.sleep(5)

        all_fav = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'All')
        all_fav.click()

    @allure.step("Number of Favourites")
    def test_17_FavList(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10)

        self.favorites_text = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View['
                                                                                         '@content-desc'
                                                                                         '="Favourites"]')))

        # Assertion: Check if the "Favorites" text is displayed
        assert self.favorites_text.is_displayed(), "Text 'Favourites' not displayed"

    @allure.step("Click on Home")
    def test_18_HomeBtn(self):

        # Home page

        wait = WebDriverWait(self.driver, 10)

        self.home_btn = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView['
                                                                                   '@content-desc="Home"]')))

        self.home_btn.click()
        time.sleep(3)

        assert self.home_btn.is_displayed(), "Text 'All Deals' All Deals 'not found"

    @allure.step("Click on the next button for Vendors shown on Dashboard ")
    def test_19_NextBtn(self):
        time.sleep(3)
        next_btn = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.widget.FrameLayout/android.view'
                                                            '.View/android.view.View/android.view.View/android.view'
                                                            '.View/android.widget.ScrollView/android.widget'
                                                            '.ImageView[4]')
        for _ in range(4):  # Click the item four times
            next_btn.click()

    @allure.step("Click view all ")
    def test_20_ViewAll(self):
        time.sleep(3)
        view_all = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'View all')
        view_all.click()
        time.sleep(3)

    @allure.step("Assert List of Partners")
    def test_21_AssertListOfPartners(self):
        WebDriverWait(self.driver, 10)

        def scroll_to_bottom():
            for _ in range(1):  # Scroll 1 time (adjust as needed)
                # Define the coordinates for the scroll action
                start_x = 500  # Adjust this value based on your app's layout
                start_y = 1600  # Adjust this value based on your app's layout
                end_y = 200  # Adjust this value based on your app's layout

                # Perform the scroll action
                action = TouchAction(self.driver)
                action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

        expected_partner_ids = ["Goil", "Banana Home", "Starlite", "Star Oil", "Barcelos", "Golden Eagle Cinema",
                                "iStore", "Melcom", "Shoprite", "Tecno", "Telefonika", "Silverbird Cinemas",
                                "Compu-Ghana", "Chicken Inn"]

        scroll_to_bottom()

        # Iterate through the expected company IDs and check if they are present
        for partner_id in expected_partner_ids:
            try:
                self.driver.find_element(MobileBy.ACCESSIBILITY_ID, partner_id)
            except NoSuchElementException:
                assert False, f"Company with ID '{partner_id}' not found"

    @allure.step("Sort List of Partners A-Z")
    def test_22_SortListAtoZ(self):
        WebDriverWait(self.driver, 10)

        # Locate the sort button and click it
        sort_button = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Sort by")
        sort_button.click()

        # Locate the "A-Z" sort option and click it
        sort_option_az = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Name (A - Z)")
        sort_option_az.click()
        time.sleep(3)

        # Get the list of company names after sorting
        sorted_company_names = self.get_company_names()

        # Assertion: Check if the list is sorted in ascending alphabetical order
        assert sorted_company_names == sorted(sorted_company_names), "List is not sorted A-Z"

    @allure.step("Sort List of Partners Z-A")
    def test_23_SortListZtoA(self):
        WebDriverWait(self.driver, 10)
        time.sleep(5)

        # Locate the sort button and click it
        sort_button = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Name (A - '
                                                               'Z)"]')
        sort_button.click()

        # Locate the "Z-A" sort option and click it
        sort_option_za = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Name (Z - A)")
        sort_option_za.click()
        time.sleep(2)

        # Get the list of company names after sorting
        sorted_company_names = self.get_company_names()

        # Assertion: Check if the list is sorted in descending alphabetical order
        assert sorted_company_names == sorted(sorted_company_names, reverse=True), "List is not sorted Z-A"

    def get_company_names(self):
        company_names = []

        # Iterate through company elements and extract names
        for company_id in ["Goil", "Banana Home", "Starlite", "Star Oil", "Barcelos", "Golden Eagle Cinema",
                           "iStore", "Melcom", "Shoprite", "Tecno", "Telefonika", "Silverbird Cinemas",
                           "Compu-Ghana", "Chicken Inn"]:
            try:
                company_element = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, company_id)
                company_names.append(company_element.text)
            except NoSuchElementException:
                pass  # Handle element not found if needed

        return company_names
