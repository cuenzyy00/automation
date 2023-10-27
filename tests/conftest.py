from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:/Users/vince/PycharmProjects/browserDrivers/chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument('--profile-directory=Profile 1')
        options.add_argument('--user-data-dir=C:\\Users\\vince\\AppData\\Local\\Google\\Chrome\\User Data\\Vincent')
        driver = webdriver.Chrome(service=service_obj, options=options)
        driver.maximize_window()
    elif browser_name == "firefox":
        service_obj = Service("C:/Users/vince/PycharmProjects/browserDrivers/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()



