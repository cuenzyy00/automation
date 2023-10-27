import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self):
        homePage = HomePage(self.driver)
        homePage.send_Name().send_keys("Vincent Cuenza")
        homePage.send_Email().send_keys("asdasdas@gmail.com")
        homePage.send_Password().send_keys("Aa1234567890!")
        homePage.click_Radio01().click()
        homePage.select_Gender().send_keys("Male")
        homePage.click_Employee().click()
        homePage.set_Date().send_keys("20/10/2023")
        homePage.click_Submit().click()
        time.sleep(2)
        message = homePage.find_Success().text
        print(message)
        assert "Success" in message
        # driver.find_element(By.XPATH, "//form/div[3]/input[1]").send_keys("Vincent Cuenza")




