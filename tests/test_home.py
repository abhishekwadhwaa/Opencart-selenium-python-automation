from pages.home_page import HomePage

def test_search_product(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_