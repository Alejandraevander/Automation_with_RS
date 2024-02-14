import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logging
import inspect

@pytest.mark.usefixtures("setup")
class BaseClass:
    
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler) #filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    
    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,text)))
        
    def selectOptionByText(self,locator,text):
        #Static Dropdown
        dropdown = Select(locator)
        dropdown.select_by_index(1)
        dropdown.select_by_visible_text(text)
