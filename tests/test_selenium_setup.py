def test_open_browser(driver):

    driver.get("https://demo.opencart.com/")

    assert driver.current_url == "https://demo.opencart.com/"
