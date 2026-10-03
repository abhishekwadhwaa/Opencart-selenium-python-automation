from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:

    PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-layout .caption h4 a") # It will find all product names.

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_product_names(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_NAMES)
        )

        return [product.text for product in products]

    def is_product_displayed(self, product_name):
        product_names = self.get_product_names()
        
        return product_name in product_names