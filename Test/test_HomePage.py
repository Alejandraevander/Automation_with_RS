import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestHomePage(BaseClass):
    
    def test_formSubmission(self):

        homepage = HomePage(self.driver)
        homepage.getEmail().send_keys("hello@gmail.com")
        homepage.getPassword().send_keys("123456")
        homepage.getCheckbutton().click()
        
        #css-selector
        homepage.getName().send_keys("Alejandra")
        homepage.getOption().click()
        homepage.getSubmit().click()
        message = homepage.getSuccessText().text
        print(message)
        assert "Success" in message
        