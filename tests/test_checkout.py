import pytest
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_checkout_selection(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=checkout/cart")

    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Checkout"))
    )
    checkout_button.click()

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()

    assert checkout_page.is_billing_details_displayed()

def test_required_billing_fields_validation(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

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

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

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

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()
    checkout_page.select_guest_checkout()

    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    assert checkout_page.is_payment_method_displayed()

@pytest.mark.xfail(
    reason="Known website bug: No payment methods available (reported in Jira)",
    strict=True
)
def test_payment_method_available(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()
    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    assert checkout_page.is_payment_method_available(), \
        "No payment method is available during checkout"


def test_payment_unavailable_warning(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

    checkout_page.select_guest_checkout()
    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    warning = checkout_page.get_payment_warning()

    assert "No Payment options are available" in warning

def test_enter_order_comment(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()
    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    checkout_page.enter_order_comment("Please deliver carefully.")

    assert checkout_page.get_order_comment() == "Please deliver carefully."

def test_terms_conditions_required(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()
    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    checkout_page.continue_without_agreeing()

    assert "You must agree to the Terms & Conditions!" in checkout_page.get_payment_error()


def test_payment_method_required(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()
    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    checkout_page.continue_with_agreement()

    assert "Payment method required!" in checkout_page.get_payment_error()  

def test_confirm_order_blocked_without_payment(driver):
    home_page = HomePage(driver)
    home_page.open()

    home_page.search_product("iPod Nano").open_product("iPod Nano").add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.open_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.select_guest_checkout()
    checkout_page.fill_billing_details("testuser123@gmail.com")
    checkout_page.submit_empty_billing_form()

    checkout_page.continue_with_agreement()

    assert "Payment method required!" in checkout_page.get_payment_error()
    assert checkout_page.is_confirm_order_collapsed()