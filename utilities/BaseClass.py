import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.mark.usefixtures('setup')
class BaseClass:

    def __init__(self):
        self.driver = None
    def verifyLinkPresence(self, text):
        SelectCountry = WebDriverWait(self.driver, 10)
        SelectCountry.until(ec.presence_of_element_located((By.LINK_TEXT, text)))

