from pages.cart_page import CartPage
from pages.home_page import HomePage


def test_product_displayed_in_cart(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")
    product_page.add_to_cart()

    cart_page = CartPage(driver)
    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=checkout/cart")

    assert any(
        "MacBook" in name
        for name in cart_page.get_product_names()
    )


def test_product_quantity_in_cart(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")
    product_page.add_to_cart()

    cart_page = CartPage(driver)
    driver.get(
        "https://naveenautomationlabs.com/opencart/index.php?route=checkout/cart"
    )

    assert cart_page.get_quantity() == "1"


def test_update_product_quantity(driver):
    home_page = HomePage(driver)
    home_page.open()

    search_results_page = home_page.search_product("MacBook")
    product_page = search_results_page.open_product("MacBook")
    product_page.add_to_cart()

    cart_page = CartPage(driver)
    driver.get(
        "https://naveenautomationlabs.com/opencart/index.php?route=checkout/cart"
    )

    cart_page.update_quantity(2)

    assert cart_page.get_quantity() == "2"



def test_remove_product_from_cart(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.search_product("MacBook").open_product("MacBook").add_to_cart()

    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=checkout/cart")

    cart_page = CartPage(driver)
    print("Products in cart:", cart_page.get_product_names())
    assert any("MacBook" in name for name in cart_page.get_product_names())

    cart_page.remove_product()

    assert cart_page.is_product_removed("MacBook")

