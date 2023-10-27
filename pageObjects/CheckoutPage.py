from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
    mobileCard = (By.XPATH, "//div[@class='card h-100']")
    clickAdd = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    clickCheckout = (By.XPATH, "(//button[@type='button'])[4]")

    def mobile_Card(self):
        return self.driver.find_elements(*CheckoutPage.mobileCard)

    def click_Add(self):
        return self.driver.find_element(*CheckoutPage.clickAdd)

    def click_Checkout(self):
        return self.driver.find_element(*CheckoutPage.clickCheckout)


