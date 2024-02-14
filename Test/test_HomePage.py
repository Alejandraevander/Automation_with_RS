import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
class TestHomePage(BaseClass):
    
    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getEmail().send_keys(getData["email"])
        log.info("Email Entered : " + getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        log.info("Password Entered : " + getData["password"])
        homepage.getCheckbutton().click()
        
        #css-selector
        homepage.getName().send_keys(getData["name"])
        log.info("Name Entered :" + getData["name"])
        homepage.getOption().click()
        self.selectOptionByText(homepage.getFormSelect(),getData["gender"])
        homepage.getSubmit().click()
        message = homepage.getSuccessText().text
        print(message)
        log.info("Message : " + message)
        assert "Success" in message
        self.driver.refresh()
        
    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self,request):
        return request.param