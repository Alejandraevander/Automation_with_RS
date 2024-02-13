from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

class ConfirmPage():
    
        def __init__(self,driver):
            self.driver = driver
            
        #self.driver.find_element(By.ID, "country").send_keys("Ind")
        #self.driver.find_element(By.LINK_TEXT,"India").click()
        #self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        #self.driver.find_element(By.XPATH,"//input[@type='submit']").click()
        #successtext = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        
        Country = (By.ID,"country")
        ChooseCountry = (By.LINK_TEXT, "India")
        CheckBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        SubmitButton = (By.XPATH, "//input[@value='Purchase']")
        #SubmitButton = (By.XPATH, "//input[@type='submit']")
        SuccessText = (By.CLASS_NAME, "alert-success")
        
        def getCountry(self):
            return self.driver.find_element(*ConfirmPage.Country)
        
        def getChooseCountry(self):
            return self.driver.find_element(*ConfirmPage.ChooseCountry)
        
        def getCheckBox(self):
            return self.driver.find_element(*ConfirmPage.CheckBox)
        
        def getSubmitButton(self):
            return self.driver.find_element(*ConfirmPage.SubmitButton)
        
        def getSuccessText(self):
            return self.driver.find_element(*ConfirmPage.SuccessText)
            