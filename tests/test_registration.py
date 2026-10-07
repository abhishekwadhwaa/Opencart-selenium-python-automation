from pages.registration_page import RegistrationPage
from utils.data_generator import generate_unique_email

def test_successful_registration(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open()

    email = generate_unique_email()

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