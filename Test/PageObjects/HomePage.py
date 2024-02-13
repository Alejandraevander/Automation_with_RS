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
    
    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage