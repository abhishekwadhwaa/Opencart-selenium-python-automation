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

def test_search_partial_keyword(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("Mac")

    assert search_results_page.is_product_displayed("MacBook")

def test_empty_search(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("")

    assert search_results_page.is_no_results_message_displayed()

def test_search_case_insensitive(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("macbook")

    assert search_results_page.is_product_displayed("MacBook")