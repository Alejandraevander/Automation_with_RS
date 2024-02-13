import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):
    
    def test_formSubmission(self):
        #Compulsory Code
        options_obj = webdriver.EdgeOptions()
        service_obj = Service(r"H:\Python_Project\Section_9_RS_Testing_Framework\edgedriver_win64\msedgedriver.exe")

        #Code to disable devtools listening on ....
        options_obj.add_experimental_option('excludeSwitches', ['enable-logging'])
        #options.add_argument("--headless=new")
        options_obj.add_argument("--guest")
        #options_obj.add_argument("windows-size=1920x1080")

        #Initialize Web Driver
        driver = webdriver.Edge(service=service_obj, options=options_obj)
        driver.maximize_window()
        #Go to Website & Starting Automation
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        time.sleep(5)
        driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
        time.sleep(5)
        driver.find_element(By.ID,"exampleCheck1").click()
        time.sleep(5)

        #Static Dropdown
        dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_index(1)
        time.sleep(5)
        dropdown.select_by_visible_text("Male")
        time.sleep(5)

        #css-selector
        driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Alejandra")
        driver.find_element(By.CSS_SELECTOR,"input[value='option1']").click()
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message