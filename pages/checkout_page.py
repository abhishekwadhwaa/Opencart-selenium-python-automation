from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException

class CheckoutPage:
    GUEST_CHECKOUT = (By.CSS_SELECTOR, "input[name='account'][value='guest']")
    CONTINUE_BUTTON = (By.ID, "button-account")
    BILLING_DETAILS = (By.ID, "collapse-payment-address")
    BILLING_CONTINUE_BUTTON = (By.ID, "button-guest")
    VALIDATION_ERRORS = (By.CSS_SELECTOR, "#collapse-payment-address .text-danger")
    FIRST_NAME = (By.ID, "input-payment-firstname")
    LAST_NAME = (By.ID, "input-payment-lastname")
    EMAIL = (By.ID, "input-payment-email")
    TELEPHONE = (By.ID, "input-payment-telephone")
    ADDRESS_1 = (By.ID, "input-payment-address-1")
    CITY = (By.ID, "input-payment-city")
    POSTCODE = (By.ID, "input-payment-postcode")
    COUNTRY = (By.ID, "input-payment-country")
    REGION = (By.ID, "input-payment-zone")
    PAYMENT_METHOD_SECTION = (By.ID, "collapse-payment-method")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver, 10,
            ignored_exceptions=(StaleElementReferenceException,)
        )

    def select_guest_checkout(self):
        guest_radio = self.wait.until(
            EC.element_to_be_clickable(self.GUEST_CHECKOUT)
        )
        guest_radio.click()

        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()

    def is_billing_details_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.BILLING_DETAILS)
        ).is_displayed()

    def submit_empty_billing_form(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.BILLING_CONTINUE_BUTTON)
        )
        continue_button.click()

    def get_billing_validation_errors(self):
        self.wait.until(
            EC.visibility_of_element_located(self.VALIDATION_ERRORS)
        )
        return [
            error.text
            for error in self.driver.find_elements(*self.VALIDATION_ERRORS)
            if error.is_displayed()
        ]

    def fill_billing_details(self, email):
        fields = [
            (self.FIRST_NAME, "Test"),
            (self.LAST_NAME, "User"),
            (self.EMAIL, email),
            (self.TELEPHONE, "9876543210"),
            (self.ADDRESS_1, "123 Test Street"),
            (self.CITY, "Gurgaon"),
            (self.POSTCODE, "122001")
        ]

        for locator, value in fields:
            field = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            field.clear()
            field.send_keys(value)

        country = Select(self.wait.until(
            EC.element_to_be_clickable(self.COUNTRY)
        ))
        country.select_by_visible_text("India")

        self.wait.until(
            lambda driver: any(
                option.text.strip() == "Haryana"
                for option in Select(driver.find_element(*self.REGION)).options
            ),
            message="Haryana did not appear in the Region dropdown"
        )

        region = Select(self.driver.find_element(*self.REGION))
        region.select_by_visible_text("Haryana")

    def is_payment_method_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PAYMENT_METHOD_SECTION)
        ).is_displayed()