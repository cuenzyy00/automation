from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        # importing page objects
        homePage = HomePage(self.driver)

        self.driver.implicitly_wait(20)

        # click shop button in landing page
        homePage.shopItems().click()

        # find the mobileCard
        findItems = homePage.mobileCard
        # findItems = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for FindingItem in findItems:
            ProductName = FindingItem.find_element(By.XPATH, "div/h4/a").text
            if ProductName == "Blackberry":
                FindingItem.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.XPATH, "(//button[@type='button'])[4]").click()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")

        SelectCountry = WebDriverWait(self.driver, 10)
        SelectCountry.until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        successPrompt = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

        assert "Success! Thank you!" in successPrompt

        time.sleep(10)
