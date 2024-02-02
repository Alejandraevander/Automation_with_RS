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
#options.add_argument("--headless=new")
options_obj.add_argument("--guest")
options_obj.add_argument("windows-size=1920x1080")

#Initialize Web Driver
driver = webdriver.Edge(service=service_obj, options=options_obj)
driver.implicitly_wait(5)

#Start Calling Website & Program
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#for whatever action, need to have perform at the end
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
#action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(5)