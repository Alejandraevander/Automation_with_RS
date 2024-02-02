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
driver.get("https://the-internet.herokuapp.com/windows")

#Handling Child Windows
driver.find_element(By.LINK_TEXT,"Click Here").click()

#Switching to different windows
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close() #only close child window

driver.switch_to.window(windows_opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

