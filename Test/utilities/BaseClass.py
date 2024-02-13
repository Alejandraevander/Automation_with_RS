import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,text)))