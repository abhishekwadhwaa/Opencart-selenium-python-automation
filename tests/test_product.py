from pages.home_page import HomePage


def test_product_name_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")

    assert product_page.get_product_name() == "MacBook"

def test_product_price_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")

    assert product_page.get_product_price() == "$602.00"

def test_product_description_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")

    assert "Intel Core 2 Duo processor" in product_page.get_product_description()

def test_product_image_displayed(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")

    assert product_page.is_product_image_displayed()

def test_add_to_cart(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")

    product_page.add_to_cart()