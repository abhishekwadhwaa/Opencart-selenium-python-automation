from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:

    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    TELEPHONE = (By.NAME, "telephone")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirm")
    PRIVACY_POLICY = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(
            "https://naveenautomationlabs.com/opencart/index.php?route=account/register"
        )

    def register(self, first_name, last_name, email, telephone, password):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

        self.driver.find_element(*self.EMAIL).send_keys(email)

        self.driver.find_element(*self.TELEPHONE).send_keys(telephone)

        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)

        self.driver.find_element(*self.PRIVACY_POLICY).click()

        self.driver.find_element(*self.CONTINUE_BUTTON).click()


    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content h1")

    def is_registration_successful(self):
        success_message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )

        return success_message.text == "Your Account Has Been Created!" 

    FIRST_NAME_ERROR = (By.CSS_SELECTOR, "#input-firstname + div.text-danger")

    def is_first_name_error_displayed(self):
        return self.wait.until(
            EC.visibility_of_all_elements_located(self.FIRST_NAME_ERROR)
        )

    def submit_empty_form(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
    