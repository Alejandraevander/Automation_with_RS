from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time
import pytest 
from PageObjects.CheckoutPage import CheckoutPage

class HomePage:
    
    def __init__(self,driver):
        self.driver = driver
    
    shop=(By.LINK_TEXT,"Shop")
    #driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
    email=(By.NAME,"email")
    password = (By.ID,"exampleInputPassword1")
    checkbutton = (By.ID,"exampleCheck1")
    name = (By.CSS_SELECTOR,"input[name='name']")
    option = (By.CSS_SELECTOR,"input[value='option1']")
    submit= (By.XPATH,"//input[@type='submit']")
    formselect = (By.ID, "exampleFormControlSelect1")
    successmessage = (By.CLASS_NAME, "alert-success")
    
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
    
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    
    def getCheckbutton(self):
        return self.driver.find_element(*HomePage.checkbutton)
    
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    
    def getOption(self):
        return self.driver.find_element(*HomePage.option)
    
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    
    def getFormSelect(self):
        return self.driver.find_element(*HomePage.formselect)
    
    def getSuccessText(self):
        return self.driver.find_element(*HomePage.successmessage)