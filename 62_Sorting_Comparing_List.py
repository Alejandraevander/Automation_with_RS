from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
import time

#Compulsory Code
options_obj = webdriver.EdgeOptions()
service_obj = Service(r"H:\Python_Project\Section_9_RS_Testing_Framework\edgedriver_win64\msedgedriver.exe")

#Code to disable devtools listening on ....
options_obj.add_experimental_option('excludeSwitches', ['enable-logging'])
#options_obj.add_argument("--headless=new")
#options_obj.add_argument("headless")
#options_obj.add_argument("--ignore-certificate-errors")
options_obj.add_argument("--guest")
options_obj.add_argument("windows-size=1920x1080")

BrowserSortedList =[]
#Initialize Web Driver
driver = webdriver.Edge(service=service_obj, options=options_obj)
driver.implicitly_wait(5)

#Start Calling Website & Program
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()
#time.sleep(10)
veggieElem = driver.find_elements(By.XPATH,"//tr/td[1]")
for elem in veggieElem:
    BrowserSortedList.append(elem.text)

ActualList = BrowserSortedList.copy()

BrowserSortedList.sort()
print(ActualList)
print(BrowserSortedList)
assert BrowserSortedList == ActualList