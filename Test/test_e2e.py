from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time
import pytest 
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        confirmpage = ConfirmPage(self.driver)
        
        i = -1
        for card in cards:
            i = i +1
            cardText = card.text
            #print(cardText)
            log.info("cardText")
            if cardText =="Blackberry":
                checkoutpage.getCardFooter()[i].click()
                
        checkoutpage.getNavigationLink().click()
        checkoutpage.getCheckout().click()
        log.info("Entering Country details")
        confirmpage.getCountry().send_keys("Ind")
        self.verifyLinkPresence("India")
        confirmpage.getChooseCountry().click()
        confirmpage.getCheckBox().click()
        confirmpage.getSubmitButton().click()
        successtext = confirmpage.getSuccessText().text
        log.info("Text Received " + successtext)
        assert "Success!21" in successtext
        time.sleep(5)   