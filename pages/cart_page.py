from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    PRODUCT_NAMES = (By.CSS_SELECTOR, "td.text-left a")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_names(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )
        return [product.text for product in products]

    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[name^='quantity']")

    def get_quantity(self):
        quantity = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT)
        )
        return quantity.get_attribute("value")

    UPDATE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Update']")

    def update_quantity(self, quantity):
        quantity_input = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT)
        )
        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

        self.driver.find_element(*self.UPDATE_BUTTON).click()

    REMOVE_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Remove']")

    def remove_product(self):
        remove_button = self.wait.until(
            EC.element_to_be_clickable(self.REMOVE_BUTTON)
        )
        remove_button.click()

    def is_product_removed(self, product_name):
        return self.wait.until(
            lambda driver: not any(
                product_name in element.text
                for element in driver.find_elements(*self.PRODUCT_NAMES)
            )
        )