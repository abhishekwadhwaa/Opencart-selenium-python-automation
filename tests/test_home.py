from pages.home_page import HomePage


def test_search_product(driver):
    home_page = HomePage(driver)

    home_page.open()

    search_results_page = home_page.search_product("MacBook")

    assert search_results_page.is_product_displayed("MacBook")

def test_search_nonexistent_product(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("adksjbgf")

    assert search_results_page.is_no_results_message_displayed()