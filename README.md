# OpenCart Selenium Python Automation Framework

## Project Overview

A web automation testing project built using **Python, Selenium WebDriver, Pytest, and the Page Object Model (POM)**.

The project automates core e-commerce functionality of the OpenCart demo website.

**Application Under Test:** https://naveenautomationlabs.com/opencart/

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git & GitHub

## Test Modules

| Module | Test Coverage |
|---|---|
| Registration | User registration |
| Login | User authentication |
| Search | Product search |
| Product Details | Product information and add to cart |
| Shopping Cart | Cart functionality |
| Checkout | Guest checkout, billing validation, payment validation |

## Framework Features

- Page Object Model for reusable page actions
- Pytest-based test execution and assertions
- Explicit waits for dynamic elements
- Positive and negative test scenarios
- Known application defect tracked using Pytest XFAIL

## Project Structure

```text
Opencart-selenium-python-automation/
├── pages/
├── tests/
├── test_data/
├── conftest.py
├── pytest.ini
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd Opencart-selenium-python-automation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install selenium pytest
```

## Running Tests

Run all tests:

```bash
pytest -v
```

## Known Application Issue

The OpenCart demo application currently does not provide an available payment method during guest checkout.

The corresponding test is marked with `pytest.mark.xfail` to document the known defect while preserving test coverage.

## Future Improvements

- HTML and Allure reporting
- GitHub Actions CI/CD integration
- Cross-browser execution
- Additional e-commerce test coverage
