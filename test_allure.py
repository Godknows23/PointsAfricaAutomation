import time
import unittest
import allure
import pytest
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
                "appium:app": "C:\\Users\\godknows_velocityinc\\Downloads\\latestProduction.apk"
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

    @allure.story("Click on Sign In button")
    def test_01_sign_in(self):
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
        self.driver.hide_keyboard()

        # Show password eye
        wait = WebDriverWait(self.driver, 5)
        time.sleep(2)

        pass_eye = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout'
                                                                          '/android.widget'
                                                                          '.LinearLayout'
                                                                          '/android.widget.FrameLayout/android.widget'
                                                                          '.FrameLayout'
                                                                          '/android.widget'
                                                                          '.FrameLayout/android.view.View/android'
                                                                          '.view.View/android'
                                                                          '.view'
                                                                          '.View'
                                                                          '/android.view.View/android.view.View'
                                                                          '/android.view.View'
                                                                          '/android.widget'
                                                                          '.EditText[2]/android.widget.ImageView')))

        pass_eye.click()
        time.sleep(3)

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

        WebDriverWait(self.driver, 5)

    @allure.step("Activate Biometrics")
    def test_08_BiometricsActive(self):
        # clear the biometrics pop-up(Activate)
        wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed

        activate_btn = wait.until(EC.element_to_be_clickable((MobileBy.XPATH, '//android.view.View['
                                                                              '@content-desc="Activate"]')))
        activate_btn.click()
        # activate_btn = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Activate"]')
        # activate_btn.click()
        WebDriverWait(self.driver, 3)
        time.sleep(3)

    @allure.testcase("Scroll on deals")
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

    @allure.story("Click on the Navigation drawer")
    @allure.testcase("Navigation drawer items")
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

        WebDriverWait(self.driver, 3)

    @allure.step("Transaction History page")
    def test_11_TransactionHistoryPage(self):

        # click on the Transaction history link
        self.driver.implicitly_wait(10)
        trans_history = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Transaction History')
        trans_history.click()
        time.sleep(3)
        # Assertion: Check if both texts are present
        points_xpath = '//android.view.View[@content-desc="Points"]'
        transactions_xpath = '//android.view.View[@content-desc="Transactions"]'
        assert self.is_text_present(points_xpath), "Points is not present"
        assert self.is_text_present(transactions_xpath), "Transactions is not present"

    def is_text_present(self, xpath):
        try:
            self.driver.find_element(MobileBy.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    @allure.step("Transaction History filters")
    def test_12_TransHistoryOffersRewards(self):
        WebDriverWait(self.driver, 2)
        offers_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Offers')
        offers_filter.click()
        time.sleep(2)

        rewards_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Rewards')
        rewards_filter.click()
        time.sleep(1)

        all_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'All')
        all_filter.click()
        time.sleep(1)

    @allure.step("Transaction History filters Corner Icon click ---- Check 'Filters & Clear All' Texts Availability")
    def test_13_TransHistoryFilterIcon(self):
        WebDriverWait(self.driver, 2)
        corner_filter = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android'
                                                                 '.widget.LinearLayout/android.widget.FrameLayout'
                                                                 '/android.widget.FrameLayout/android.widget'
                                                                 '.FrameLayout/android.view.View/android.view.View'
                                                                 '/android.view.View/android.view.View/android.widget'
                                                                 '.ScrollView/android.widget.ImageView')
        corner_filter.click()
        time.sleep(2)
        filters_xpath = '//android.view.View[@content-desc="Filters"]'
        clear_xpath = '//android.widget.Button[@content-desc="Clear all"]'
        assert self.is_statement_present(filters_xpath), "Filters is not present"
        assert self.is_statement_present(clear_xpath), "Clear all is not present"

    def is_statement_present(self, xpath):
        try:
            self.driver.find_element(MobileBy.XPATH, xpath)
            return True
        except NoSuchElementException:
            return False

    @allure.step("Transaction History filters by Date")
    def test_14_TransHistoryAllFilters(self):
        WebDriverWait(self.driver, 2)
        date_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Date')
        date_filter.click()
        time.sleep(2)
        start_date = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Start Date')
        start_date.click()
        time.sleep(2)

        back_august = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Backward')
        back_august.click()

        WebDriverWait(self.driver, 2)
        choose_date = self.driver.find_element(MobileBy.XPATH, '//android.view.View'
                                                               '[@content-desc="Sun, 20 August 2023"]')
        choose_date.click()
        ok_date = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'OK')
        ok_date.click()

        # click on end date

        time.sleep(2)
        end_date = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'End Date')
        end_date.click()
        time.sleep(2)
        select_date = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Fri, 01 September '
                                                               '2023"]')
        select_date.click()
        click_ok = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'OK')
        click_ok.click()
        time.sleep(2)
        hide_filter = self.driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="Text to '
                                                               'announce in accessibility modes"]')
        hide_filter.click()
        WebDriverWait(self.driver, 3)
        time.sleep(3)

    @allure.step("Transaction History filter by Points")
    @pytest.mark.skip("Test is skipped due to level of difficult on the points filter")
    def test_14_TransHistoryPointsFilter(self):
        WebDriverWait(self.driver, 2)
        home = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.FrameLayout/android.widget.FrameLayout/android.view.View'
                                                        '/android.view.View/android.view.View/android.view.View'
                                                        '/android.view.View[1]/android.widget.ImageView')
        home.click()
        time.sleep(2)

        clear_all = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Clear all')
        clear_all.click()
        WebDriverWait(self.driver, 5)
        time.sleep(1)

    @allure.step("Transaction History filter by Amount")
    def test_15_TransHistoryAmountFilter(self):
        WebDriverWait(self.driver, 2)

        main_filter = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                               '.LinearLayout/android.widget.FrameLayout/android'
                                                               '.widget.FrameLayout/android.widget.FrameLayout'
                                                               '/android.view.View/android.view.View/android.view'
                                                               '.View/android.view.View/android.widget.ScrollView'
                                                               '/android.widget.ImageView')
        main_filter.click()
        self.driver.implicitly_wait(4)
        self.driver.find_elements(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                  '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                  '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                  '.view.View[1]/android.view.View/android.widget.ScrollView')

        # Swipe from the bottom of the screen to the top
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=100)
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=100)

        amount_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Amount')
        amount_filter.click()
        time.sleep(2)

        start_amount = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.widget.FrameLayout/android.view'
                                                            '.View/android.view.View/android.view.View['
                                                            '1]/android.view.View/android.widget.ScrollView/android'
                                                            '.widget.EditText[1]'))
        )

        # Use TouchAction to simulate a tap on the input field
        TouchAction(self.driver).tap(start_amount).perform()

        ghs_amount = "100"
        start_amount.send_keys(ghs_amount)

        # Hide the keyboard if needed
        self.driver.press_keycode(66)  # 4 corresponds to the "Back" key

        self.driver.implicitly_wait(3)

        max_amount = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.widget.FrameLayout/android.view'
                                                            '.View/android.view.View/android.view.View['
                                                            '1]/android.view.View/android.widget.ScrollView/android'
                                                            '.widget.EditText[2]'))
        )

        # Use TouchAction to simulate a tap on the input field
        TouchAction(self.driver).tap(max_amount).perform()

        amount = "1500"
        max_amount.send_keys(amount)

        # Hide the keyboard if needed
        self.driver.press_keycode(66)

        self.driver.implicitly_wait(3)

        time.sleep(1)
        close_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Text to announce in accessibility modes')
        close_filter.click()
        time.sleep(3)

    @allure.step("Filter by Partners")
    def test_16_FilterByPartners(self):

        self.driver.implicitly_wait(3)
        main = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.FrameLayout/android.widget.FrameLayout/android.view.View'
                                                        '/android.view.View/android.view.View/android.view.View'
                                                        '/android.widget.ScrollView/android.widget.ImageView')

        main.click()

        clear_all = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Clear all')
        clear_all.click()
        WebDriverWait(self.driver, 2)
        main.click()

        partners_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Partners')
        partners_filter.click()
        WebDriverWait(self.driver, 2)

        self.driver.find_elements(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                  '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                  '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                  '.view.View[1]/android.view.View/android.widget.ScrollView')

        # Swipe from the bottom of the screen to the top
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=400)
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=400)

        WebDriverWait(self.driver, 2)
        time.sleep(3)

        check_partner1 = self.driver.find_element(MobileBy.XPATH, '//android.view.View['
                                                                  '@content-desc="Tecno"]/android.widget.ImageView[1]')
        check_partner1.click()

        WebDriverWait(self.driver, 2)

        partner2 = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Telefonika"]')
        partner2.click()
        WebDriverWait(self.driver, 2)

        time.sleep(3)

        x_btn = self.driver.find_element(MobileBy.XPATH, '//android.widget.Button[@content-desc="Text to announce in '
                                                         'accessibility modes"]')
        x_btn.click()
        WebDriverWait(self.driver, 4)

        offers = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Offers')
        offers.click()
        time.sleep(2)

        rewards = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Rewards')
        rewards.click()
        time.sleep(1)

        all_filter = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'All')
        all_filter.click()
        time.sleep(2)

        self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                 '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                 '.view.View/android.view.View/android.widget.ScrollView')

        # Swipe from the bottom of the screen to the top
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=400)
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=400)

        WebDriverWait(self.driver, 2)

        transaction_complete = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout'
                                                                        '/android.widget.LinearLayout/android.widget'
                                                                        '.FrameLayout/android.widget.FrameLayout'
                                                                        '/android.widget.FrameLayout/android.view'
                                                                        '.View/android.view.View/android.view.View'
                                                                        '/android.view.View/android.widget.ImageView['
                                                                        '1]')
        transaction_complete.click()

        WebDriverWait(self.driver, 2)

    @allure.story("Help and FAQs")
    def test_17_helpAndFaqs(self):

        help_faqs = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Help and FAQs"]')
        help_faqs.click()
        WebDriverWait(self.driver, 6)
        time.sleep(6)

        faqs_text = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'FAQs and Help')
        assert faqs_text.is_displayed(), "FAQs and Help is not displayed"

        first_faq = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="What is points '
                                                             'redemption?"]')
        first_faq.click()

        WebDriverWait(self.driver, 2)

        second_faq = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="What is meant by '
                                                              'earning  points?"]')

        second_faq.click()
        WebDriverWait(self.driver, 2)

    @allure.step("Help page navigation")
    def test_18_HelpPage(self):

        help_tab = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Help')
        help_tab.click()

        email_text = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'info@pointsafrica.com')
        assert email_text.is_displayed(), "Email Address not found on the help page"

        WebDriverWait(self.driver, 2)

        self.driver.press_keycode(4)

    @allure.step("Terms and Conditions hyperlink")
    def test_19_TermsAndConditions(self):

        WebDriverWait(self.driver, 2)
        terms_hyperlink = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Terms and Conditions')
        terms_hyperlink.click()

        terms_text = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Terms of use & Privacy')
        assert terms_text.is_displayed()
        time.sleep(5)

        self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                 '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                 '.view.View/android.view.View/android.widget.ScrollView')

        # Get the screen dimensions
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        # Swipe from the bottom of the screen to the top
        start_x = width * 0.5
        start_y = height * 0.8
        end_y = height * 0.2
        duration = 400

        # Perform the swipe gesture to scroll down
        self.driver.swipe(start_x=start_x, start_y=start_y, end_x=start_x, end_y=end_y, duration=duration)

        # Perform the swipe gesture to scroll back up to the starting point
        self.driver.swipe(start_x=start_x, start_y=end_y, end_x=start_x, end_y=start_y, duration=duration)

        # Wait for some time
        WebDriverWait(self.driver, 2)
        time.sleep(3)

        data_privacy = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Data Privacy')
        data_privacy.click()
        time.sleep(3)

        WebDriverWait(self.driver, 2)

        self.driver.press_keycode(4)

    @allure.step("Notifications page")
    def test_20_NotificationsPage(self):

        WebDriverWait(self.driver, 2)
        inbox_link = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Inbox')
        inbox_link.click()
        time.sleep(5)

        notifications_text = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Notifications')
        assert notifications_text.is_displayed(), "Notifications Text not Displayed manually check the App "

        self.driver.implicitly_wait(4)
        self.driver.find_elements(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                  '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                  '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                  '.view.View/android.view.View/android.widget.ScrollView')

        # Swipe from the bottom of the screen to the top
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=900)
        self.driver.swipe(start_x=width * 0.5, start_y=height * 0.8, end_x=width * 0.5, end_y=height * 0.2,
                          duration=900)

        self.driver.press_keycode(4)

        time.sleep(2)

    @allure.story("Edit Profile Button")
    def test_21_EditProfile(self):

        edit_profile = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Edit Profile')
        edit_profile.click()
        time.sleep(5)

        # click on change image icon
        self.driver.implicitly_wait(5)

        change_image = self.driver.find_element(MobileBy.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                '.widget.FrameLayout/android.view.View/android.view.View/android'
                                                '.view.View/android.view.View/android.view.View/android.view.View'
                                                '/android.widget.ImageView[3]')
        change_image.click()
        time.sleep(5)

    @allure.step("Test Avatar Count")
    def test_22_AvatarCount(self):
        WebDriverWait(self.driver, 10)

        # Navigate to the page with avatars

        # Define a list of 8 XPaths for avatars
        avatar_paths = [
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.widget.ImageView[1]',
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.view.View/android.widget.ImageView[1]',
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.widget.ImageView[2]',
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.widget.ImageView[3]',
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.widget.ImageView[4]',
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.widget.ImageView[5]',
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.widget.ImageView[6]',
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
            '.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View['
            '1]/android.view.View/android.widget.ScrollView/android.view.View['
            '2]/android.view.View/android.widget.ImageView[7]'
        ]

        # Initialize a count for the avatars found
        avatar_count = 0

        # Iterate through the XPaths and locate avatar elements
        for xpath in avatar_paths:
            try:
                self.driver.find_element(MobileBy.XPATH, xpath)
                avatar_count += 1
            except NoSuchElementException:
                pass  # Handle element not found if needed

        # Assertion: Check if the number of avatars is 8
        assert avatar_count == 8, "Expected 8 avatars, but found different number"
        time.sleep(1)

        # choose_avatar_text = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Choose an avatar')
        # assert choose_avatar_text.is_displayed(), "Choose an avatar text not displayed"
        # assert choose_avatar_text.text == "Choose an avatar", "Incorrect text"

    @allure.step("Test Avatar Selection")
    def test_23_AvatarSelection(self):
        self.driver.implicitly_wait(5)
        choose_image = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                                '.LinearLayout/android.widget.FrameLayout/android'
                                                                '.widget.FrameLayout/android.widget.FrameLayout'
                                                                '/android.view.View/android.view.View/android.view'
                                                                '.View['
                                                                '1]/android.view.View/android.widget.ScrollView'
                                                                '/android.view.View['
                                                                '2]/android.view.View/android.widget.ImageView[6]')
        choose_image.click()
        time.sleep(5)

        save = self.driver.find_element(MobileBy.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                        '/android.view.View/android.view.View/android.view.View/android.view.View'
                                        '/android.view.View/android.view.View/android.widget.ImageView[2]')
        save.click()

        time.sleep(5)

        cancel_btn = self.driver.find_element(MobileBy.CLASS_NAME, "android.widget.Button")
        cancel_btn.click()

    @allure.story("Click on Offers on Dashboard")
    def test_25_OffersBtn(self):
        # offers page
        time.sleep(5)
        offer_btn = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Offers"]')
        offer_btn.click()
        time.sleep(5)

    @allure.step("Click on Rewards")
    def test_26_RewardsBtn(self):
        # Rewards page
        time.sleep(5)
        offer_btn = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Rewards"]')

        offer_btn.click()

    @allure.step("Click on Favourites")
    def test_27_FavouritesBtn(self):
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
    def test_28_FavList(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10)

        self.favorites_text = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.view.View['
                                                                                         '@content-desc'
                                                                                         '="Favourites"]')))

        # Assertion: Check if the "Favorites" text is displayed
        assert self.favorites_text.is_displayed(), "Text 'Favourites' not displayed"

    @allure.step("Click on Home")
    def test_29_HomeBtn(self):

        # Home page

        wait = WebDriverWait(self.driver, 10)

        self.home_btn = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.ImageView['
                                                                                   '@content-desc="Home"]')))

        self.home_btn.click()
        time.sleep(3)

        assert self.home_btn.is_displayed(), "Text 'All Deals' All Deals 'not found"

    @allure.story("Click on the next button for Vendors shown on Dashboard ")
    def test_30_NextBtn(self):
        time.sleep(3)
        next_btn = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.widget.FrameLayout/android.view'
                                                            '.View/android.view.View/android.view.View/android.view'
                                                            '.View/android.widget.ScrollView/android.widget'
                                                            '.ImageView[4]')
        for _ in range(5):  # Click the item five times
            next_btn.click()

    def test_31_BackBtn(self):
        time.sleep(3)
        back_btn = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                            '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                            '.FrameLayout/android.widget.FrameLayout/android.view'
                                                            '.View/android.view.View/android.view.View/android.view'
                                                            '.View/android.widget.ScrollView/android.widget'
                                                            '.ImageView[3]')
        for _ in range(3):  # Click the item five times
            back_btn.click()

    @allure.step("Click view all ")
    def test_32_ViewAll(self):
        WebDriverWait(self.driver, 2)
        view_all = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'View all')
        view_all.click()
        time.sleep(3)

    @allure.step("Assert List of Partners")
    def test_33_AssertListOfPartners(self):
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
                                "Compu-Ghana", "Chicken Inn", "Vida e Caffe"]

        scroll_to_bottom()

        # Iterate through the expected company IDs and check if they are present
        for partner_id in expected_partner_ids:
            try:
                self.driver.find_element(MobileBy.ACCESSIBILITY_ID, partner_id)
            except NoSuchElementException:
                assert False, f"Company with ID '{partner_id}' not found"

    @allure.step("Sort List of Partners A-Z")
    def test_34_SortListAtoZ(self):
        WebDriverWait(self.driver, 2)

        # Locate the sort button and click it
        sort_button = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Sort by")
        sort_button.click()

        WebDriverWait(self.driver, 2)
        # Locate the "A-Z" sort option and click it
        sort_option_az = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Name (A - Z)")
        sort_option_az.click()

        # Get the list of company names after sorting
        sorted_company_names = self.get_company_names()

        # Assertion: Check if the list is sorted in ascending alphabetical order
        assert sorted_company_names == sorted(sorted_company_names), "List is not sorted A-Z"

    @allure.step("Sort List of Partners Z-A")
    def test_35_SortListZtoA(self):
        WebDriverWait(self.driver, 3)

        # Locate the sort button and click it
        sort_button = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="Name (A - '
                                                               'Z)"]')
        sort_button.click()

        # Locate the "Z-A" sort option and click it
        sort_option_za = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Name (Z - A)")
        sort_option_za.click()

        # Get the list of company names after sorting
        sorted_company_names = self.get_company_names()

        # Assertion: Check if the list is sorted in descending alphabetical order
        assert sorted_company_names == sorted(sorted_company_names, reverse=True), "List is not sorted Z-A"

    def get_company_names(self):
        company_names = []

        # Iterate through company elements and extract names
        for company_id in ["Goil", "Banana Home", "Starlite", "Star Oil", "Barcelos", "Golden Eagle Cinema",
                           "iStore", "Melcom", "Shoprite", "Tecno", "Telefonika", "Silverbird Cinemas",
                           "Compu-Ghana", "Chicken Inn", "Vida e Caffe"]:
            try:
                company_element = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, company_id)
                company_names.append(company_element.text)
            except NoSuchElementException:
                pass  # Handle element not found if needed

        return company_names

    def test_36_backAndSave(self):

        back_save = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                             '.FrameLayout/android.widget.FrameLayout/android.view'
                                                             '.View/android.view.View/android.view.View/android.view'
                                                             '.View/android.widget.ImageView[1]')
        back_save.click()
        WebDriverWait(self.driver, 2)

    @allure.story("Reward Options click ")
    def test_37_RewardsOptions(self):

        rewards_option = self.driver.find_element(MobileBy.XPATH,
                                                  '//android.widget.ImageView[@content-desc="Reward Options"]')
        rewards_option.click()

        self.driver.press_keycode(4)

        # dismiss_button = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Dismiss"]')
        # dismiss_button.click()

        WebDriverWait(self.driver, 2 )

        # self.pointsAfricaText = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,
        #                                                                    'Points Africa')))
        #
        # # Assertion: Check if the "Points Africa" text is displayed
        # assert self.pointsAfricaText.is_displayed(), "Text 'Points Africa' not displayed"

    @allure.story("Transaction flow")
    def test_38_MakeTransaction(self):
        all_partners = self.driver.find_element(MobileBy.XPATH, '//android.widget.ImageView[@content-desc="View all"]')
        all_partners.click()

        max_scrolls = 1  # Maximum number of times to scroll

        for _ in range(max_scrolls):
            try:
                melcom_partner = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Melcom")
                # If element is found, perform desired action or break the loop
                melcom_partner.click()
                break
            except NoSuchElementException:
                # Scroll action (you might need to adjust the swipe coordinates)
                self.scroll_down()
        else:
            print("Element not found after scrolling")

        wait = WebDriverWait(self.driver, 10)
        deal_element = wait.until(EC.visibility_of_element_located((MobileBy.XPATH, '//android.view.View[contains('
                                                                                    '@content-desc, "Shopping made '
                                                                                    'easier")]')))

        deal_element.click()

        WebDriverWait(self.driver, 5)

    @allure.step("Validation of the page items")
    def test_39_PageValidation(self):

        page_points = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Points / GHC')
        expiry_dates = self.driver.find_element(MobileBy.XPATH, '//android.view.View[contains(@content-desc, '
                                                                '"Expires")]')
        details_title = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Shopping made easier')
        terms_conditions = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Terms and Conditions ')

        # deal_title = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Shopping made easier')
        #
        # # Get the text from the element
        # actual_text = deal_title.text
        #
        # # Define the expected text
        # expected_text = "Shopping made easier"
        #
        # # Perform the assertion
        # self.assertEqual(actual_text, expected_text, f"Expected '{expected_text}' but got '{actual_text}'")

        assert page_points.is_displayed()
        assert expiry_dates.is_displayed()
        assert details_title.is_displayed()
        assert terms_conditions.is_displayed()

        WebDriverWait(self.driver, 3)

    @allure.step("Scan button click")
    def test_40_ScanAndMerchant(self):

        wait = WebDriverWait(self.driver, 3)
        self.scanPay = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '/hierarchy/android.widget'
                                                                                  '.FrameLayout/android.widget'
                                                                                  '.LinearLayout/android.widget'
                                                                                  '.FrameLayout/android.widget'
                                                                                  '.FrameLayout/android.widget'
                                                                                  '.FrameLayout/android.view.View'
                                                                                  '/android.view.View/android.view'
                                                                                  '.View/android.view.View/android'
                                                                                  '.widget.ImageView[4]')))
        self.scanPay.click()

        wait = WebDriverWait(self.driver, 5)
        self.popUp = wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.android.permissioncontroller:id'
                                                                             '/permission_allow_foreground_only_button'
                                                                )))
        self.popUp.click()

        wait = WebDriverWait(self.driver, 5)
        self.merchantID = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Enter merchant ID')))
        self.merchantID.click()

        self.driver.implicitly_wait(3)

        merchant_input = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Enter the '
                                                                  'vendor merchant ID to proceed"]/android.view.View['
                                                                  '3]/android.widget.EditText')

        # Use TouchAction to simulate a tap on the input field
        TouchAction(self.driver).tap(merchant_input).perform()

        enter_merchant = "196919992006"
        merchant_input.send_keys(enter_merchant)
        self.driver.implicitly_wait(3)
        self.driver.hide_keyboard()

        # self.driver.press_keycode(66)

        proceed_next = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Next')
        proceed_next.click()

        # cancel_btn = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Cancel')

        # assert cancel_btn.is_displayed()

        wait = WebDriverWait(self.driver, 5)
        self.confirm_proceed = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Confirm')))
        self.confirm_proceed.click()

    @allure.step("Payment screen ")
    def test_41_PaymentScreen(self):
        self.driver.implicitly_wait(3)
        amount_input = self.driver.find_element(MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                                '.LinearLayout/android.widget.FrameLayout/android'
                                                                '.widget.FrameLayout/android.widget.FrameLayout'
                                                                '/android.view.View/android.view.View/android.view'
                                                                '.View/android.view.View/android.view.View['
                                                                '4]/android.view.View/android.view.View/android'
                                                                '.widget.EditText')

        # Use TouchAction to simulate a tap on the input field
        TouchAction(self.driver).tap(amount_input).perform()

        enter_amount = "250"
        amount_input.send_keys(enter_amount)
        self.driver.implicitly_wait(3)
        self.driver.press_keycode(66)

        offer_checkout = self.driver.find_element(MobileBy.XPATH, '(//android.view.View[@content-desc="Offer"])[2]')
        offer_checkout.click()

    @allure.step("Payment Confirmation")
    def test_42_PaymentConfirmation(self):
        wait = WebDriverWait(self.driver, 5)
        self.confirm_payment = wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Confirm')))
        self.confirm_payment.click()

        wait = WebDriverWait(self.driver, 10)
        self.notifications_popup = wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.android'
                                                                                           '.permissioncontroller:id'
                                                                                           '/permission_allow_button')))
        self.notifications_popup.click()

        time.sleep(20)

    @allure.step("Transaction Successful Screen")
    def test_43_TransactionSuccess(self):
        WebDriverWait(self.driver, 10)
        points_earned = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="25 Points"]')
        amount_paid = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="GHC 2.50"]')
        payment_by = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="MTN card"]')
        merchant_id = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="196919992006"]')
        merchant = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Melcom"]')
        success_title = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Transaction '
                                                                 'Successful "]')

        assert points_earned.is_displayed()
        assert amount_paid.is_displayed()
        assert payment_by.is_displayed()
        assert merchant_id.is_displayed()
        assert merchant.is_displayed()
        assert success_title.is_displayed()

        WebDriverWait(self.driver, 5)
        dashboard_btn = self.driver.find_element(MobileBy.XPATH, '//android.view.View[@content-desc="Go to dashboard"]')
        dashboard_btn.click()
        time.sleep(5)







