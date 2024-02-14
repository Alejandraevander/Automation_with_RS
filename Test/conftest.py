import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="edge":
        options_obj = webdriver.EdgeOptions()
        options_obj.add_argument("--guest")
        #options_obj.add_argument("windows-size=1920x1080")
        #Code to disable devtools listening on ....
        options_obj.add_experimental_option('excludeSwitches', ['enable-logging'])
        #options_obj.add_argument("--headless=new")
        #ptions_obj.add_argument("--start-maximized")
        #options_obj.add_argument("headless")
        #options_obj.add_argument("--ignore-certificate-errors")
        service_obj = Service(r"H:\Python_Project\Section_9_RS_Testing_Framework\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj, options=options_obj)

      
       
    elif browser_name == "firefox":
        options_obj = webdriver.EdgeOptions()
        service_obj = Service(r"H:\Python_Project\Section_9_RS_Testing_Framework\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Firefox(service=service_obj, options=options_obj)

    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()


        # #Compulsory Code
        # options_obj = webdriver.EdgeOptions()
        # service_obj = Service(r"H:\Python_Project\Section_9_RS_Testing_Framework\edgedriver_win64\msedgedriver.exe")

        # #Code to disable devtools listening on ....
        # options_obj.add_experimental_option('excludeSwitches', ['enable-logging'])
        # #options.add_argument("--headless=new")
        # options_obj.add_argument("--guest")
        # #options_obj.add_argument("windows-size=1920x1080")

        # #Initialize Web Driver
        # driver = webdriver.Edge(service=service_obj, options=options_obj)
        # driver.maximize_window()
        # #Go to Website & Starting Automation
        # driver.get("https://rahulshettyacademy.com/angularpractice/")