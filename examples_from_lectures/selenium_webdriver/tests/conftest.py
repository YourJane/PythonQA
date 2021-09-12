import os
import pytest

from selenium import webdriver


DRIVERS = os.path.expanduser("/Users/jane/Courses/PythonAutomation/webdriver")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser window")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "safari"])
    parser.addoption("--url", action="store", default="https://demo.opencart.com")


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if _browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif _browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    elif _browser == "safari":
        driver = webdriver.Safari()

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()

    request.addfinalizer(final)

    return driver
