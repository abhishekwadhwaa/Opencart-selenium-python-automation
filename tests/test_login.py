from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.login_page import LoginPage
import json
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_login() #opens login via homepage

    login_page = LoginPage(driver)
    login_page.login("invalid_user@example.com", "WrongPassword123")

    assert login_page.is_error_message_displayed()


def test_login_with_empty_fields(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_login()

    login_page = LoginPage(driver)
    login_page.login("", "")

    assert login_page.is_error_message_displayed()


def test_login_with_invalid_email(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_login()

    login_page = LoginPage(driver)
    login_page.login("noafdsd@gmai.com", "abhishek@@123")

    assert login_page.is_error_message_displayed()

def test_login_with_invalid_password(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.open_login()

    login_page = LoginPage(driver)
    login_page.login("notregistered@gmail.com", "WrongPassword123")

    assert login_page.is_error_message_displayed()


def test_successful_login(driver):
    file_path = (
        Path(__file__).parent.parent
        / "test_data"
        / "test_account.json"
    )

    with open(file_path, "r") as file:
        account = json.load(file)

    home_page = HomePage(driver)
    home_page.open()
    home_page.open_login()

    login_page = LoginPage(driver)
    login_page.login(account["email"], account["password"])

    WebDriverWait(driver, 15).until(
        EC.url_contains("route=account/account")
    )

    assert "route=account/account" in driver.current_url