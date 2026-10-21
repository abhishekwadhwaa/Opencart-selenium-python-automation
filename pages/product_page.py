from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    PRODUCT_NAME = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    PRODUCT_PRICE = (By.CSS_SELECTOR, "ul.list-unstyled h2")

    def get_product_price(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_PRICE)
        ).text

    DESCRIPTION = (By.ID, "tab-description")

    def get_product_description(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.DESCRIPTION)
        ).text

    PRODUCT_IMAGE = (By.CSS_SELECTOR, "ul.thumbnails img")

    def is_product_image_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_IMAGE)
        ).is_displayed()

    ADD_TO_CART_BUTTON = (By.ID, "button-cart")

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".alert-success")
            )
        )

        self.wait.until(
            lambda driver: "1 item(s)" in driver.find_element(
                By.ID, "cart-total"
            ).text
        )

    CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

    def get_cart_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_SUCCESS_MESSAGE)
        ).text
    
    QUANTITY_FIELD = (By.ID, "input-quantity")

    def set_quantity(self, quantity):
        field = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_FIELD)
        )
        field.clear()
        field.send_keys(str(quantity))