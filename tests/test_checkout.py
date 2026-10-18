from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage


def test_guest_checkout_selection(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=checkout/checkout")

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()

    assert checkout_page.is_billing_details_displayed()

def test_required_billing_fields_validation(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=checkout/checkout")

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()
    checkout_page.submit_empty_billing_form()

    errors = checkout_page.get_billing_validation_errors()

    expected_errors = [
        "First Name must be between 1 and 32 characters!",
        "Last Name must be between 1 and 32 characters!",
        "E-Mail address does not appear to be valid!",
        "Telephone must be between 3 and 32 characters!",
        "Address 1 must be between 3 and 128 characters!",
        "City must be between 2 and 128 characters!"
    ]

    for expected_error in expected_errors:
        assert expected_error in errors


def test_invalid_billing_email(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=checkout/checkout")

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()

    checkout_page.fill_billing_details("abhishek123")
    checkout_page.submit_empty_billing_form()

    errors = checkout_page.get_billing_validation_errors()

    assert "E-Mail address does not appear to be valid!" in errors


def test_valid_billing_details(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=checkout/checkout")

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()

    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    assert checkout_page.is_payment_method_displayed()
