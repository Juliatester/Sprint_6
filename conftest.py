import pytest
from selenium import webdriver
from locators.main_page_locators import SiteHeaderLocators

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Choose browser: firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Браузер '{browser_name}' не поддерживается!")

    driver.maximize_window()
    driver.get(SiteHeaderLocators.main_url)
    yield driver
    driver.quit()