from selenium.webdriver.common.by import By


class PlaceOrderPage:
    def __init__(self, driver):
        self.driver = driver
    browseCountry = (By.XPATH, "//input[@id='country']")
    selectCountry = (By.LINK_TEXT, "India")
    tickCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    clickPurchase = (By.XPATH, "//input[@value='Purchase']")
    findSuccessPrompt = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def browse_Country(self):
        return self.driver.find_element(*PlaceOrderPage.browseCountry)

    def select_Country(self):
        return self.driver.find_element(*PlaceOrderPage.selectCountry)

    def tick_Checkbox(self):
        return self.driver.find_element(*PlaceOrderPage.tickCheckbox)

    def click_Purchase(self):
        return self.driver.find_element(*PlaceOrderPage.clickPurchase)

    def find_SuccessPrompt(self):
        return self.driver.find_element(*PlaceOrderPage.findSuccessPrompt)


