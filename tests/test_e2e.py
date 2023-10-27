import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.PlaceOrderPage import PlaceOrderPage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        # importing page objects
        homePage = HomePage(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        placeorderPage = PlaceOrderPage(self.driver)

        self.driver.implicitly_wait(20)

        # click shop button in landing page
        homePage.shop_Items().click()

        # find the mobileCard
        findItems = checkoutPage.mobile_Card()

        for FindingItem in findItems:
            ProductName = FindingItem.find_element(By.XPATH, "div/h4/a").text
            if ProductName == "Blackberry":
                FindingItem.find_element(By.XPATH, "div/button").click()

        checkoutPage.click_Add().click()
        checkoutPage.click_Checkout().click()
        placeorderPage.browse_Country().send_keys("ind")
        self.verifyLinkPresence("India")
        placeorderPage.select_Country().click()
        placeorderPage.tick_Checkbox().click()
        placeorderPage.click_Purchase().click()
        successPrompt = placeorderPage.find_SuccessPrompt().text

        assert "Success! Thank you!" in successPrompt

        time.sleep(10)
