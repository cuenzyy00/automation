from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.XPATH, "//a[contains(@href,'shop')]")
    sendName = (By.XPATH, "//form/div[1]/input[1]")
    sendEmail = (By.XPATH, "(//input[@name='email'])[1]")
    sendPassword = (By.XPATH, "(//input[@id='exampleInputPassword1'])[1]")
    clickRadio01 = (By.XPATH, "(//input[@id='exampleCheck1'])[1]")
    selectGender = (By.XPATH, "(//select[@id='exampleFormControlSelect1'])[1]")
    clickEmployee = (By.XPATH, "//form/div[6]/div[2]/input")
    setDate = (By.XPATH, "//input[@type='date']")
    clickSubmit = (By.XPATH, "(//input[@value='Submit'])[1]")
    findSuccess = (By.XPATH, "(//div[@class='alert alert-success alert-dismissible'])[1]")

    def shop_Items(self):
        return self.driver.find_element(*HomePage.shop)

    def send_Name(self):
        return self.driver.find_element(*HomePage.sendName)

    def send_Email(self):
        return self.driver.find_element(*HomePage.sendEmail)

    def send_Password(self):
        return self.driver.find_element(*HomePage.sendPassword)

    def click_Radio01(self):
        return self.driver.find_element(*HomePage.clickRadio01)

    def select_Gender(self):
        return self.driver.find_element(*HomePage.selectGender)

    def click_Employee(self):
        return self.driver.find_element(*HomePage.clickEmployee)

    def set_Date(self):
        return self.driver.find_element(*HomePage.setDate)

    def click_Submit(self):
        return self.driver.find_element(*HomePage.clickSubmit)

    def find_Success(self):
        return self.driver.find_element(*HomePage.findSuccess)
