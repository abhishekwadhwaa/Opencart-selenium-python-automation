from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.search_results_page import SearchResultsPage

class HomePage:

    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://naveenautomationlabs.com/opencart/")

    def search_product(self, product_name):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )

        search_box.send_keys(product_name)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        search_button.click()
        return SearchResultsPage(self.driver)