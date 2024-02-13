from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import ConfirmPage

class CheckoutPage:
        def __init__(self,driver):
            self.driver = driver
    
    #   self.driver.find.elements(By.CSS_SELECTOR,".card-footer button")
        cardTitle =(By.CSS_SELECTOR, ".card-title a")
        cardFooter=(By.CSS_SELECTOR, ".card-footer button")
        #self.driver.find_element(By.CSS_SELECTOR,"a[class*='nav-link btn btn-primary']").click()
        navigationLink = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")
        #self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        checkOut = (By.XPATH, "//button[@class='btn btn-success']")
        
        def getCardTitles(self):
            return self.driver.find_elements(*CheckoutPage.cardTitle)
        
        def getCardFooter(self):
            return self.driver.find_elements(*CheckoutPage.cardFooter)
        
        def getNavigationLink(self):
            return self.driver.find_element(*CheckoutPage.navigationLink)
        
        def getCheckout(self):
            return self.driver.find_element(*CheckoutPage.checkOut)