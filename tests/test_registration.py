from pages.registration_page import RegistrationPage
from utils.data_generator import generate_unique_email
import json
from pathlib import Path

def test_successful_registration(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open()

    email = generate_unique_email()

    account = {
        "first_name": "Abhishek",
        "last_name": "Wadhwa",
        "email": email, 
        "password": "Test@123",
        "telephone": "9876543210"
    }

    file_path = Path(__file__).parent.parent / "test_data" / "test_account.json"

    with open(file_path, "w") as file:
        json.dump(account, file, indent=4)

    registration_page.register(
        "Abhishek",
        "Wadhwa",
        email,
        "9876543210",
        "Test@123"
    )

    assert registration_page.is_registration_successful()

def test_required_fields_validation(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open()

    registration_page.submit_empty_form()

    assert registration_page.is_first_name_error_displayed()

def test_invalid_email_format(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open()

    registration_page.register(
        "Abhishek",
        "Wadhwa",
        "invalid-email",
        "9876543210",
        "Test@123"
    )

    assert registration_page.driver.current_url.endswith(
        "route=account/register"
    )

def test_password_mismatch(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open()

    registration_page.register(
        "Abhishek",
        "Wadhwa",
        "test@gmail.com",
        "974134137",
        "Test@123",
        "Test@456"
    )

    assert registration_page.is_confirm_password_error_displayed()


def test_duplicate_email(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open()

    registration_page.register(
        "Abhishek",
        "Wadhwa",
        "abhishek@gmail.com",
        "9876543210",
        "Test@123"
    )

    assert registration_page.is_duplicate_email_error_displayed()
