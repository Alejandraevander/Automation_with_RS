from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
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

#Start Calling Website & Program
driver.get("https://rahulshettyacademy.com/client")
time.sleep(5)

#By Using Link Text (with "a" html attributes)
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(5)

#By Using XPATH
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("alejandra.evander92@gmail.com")
time.sleep(5)

#By Using CSS_SELECTOR, same as xpath but remove first // and replace / with space " " and div -> div:nth-child(x)
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("12345678aA")
time.sleep(5)

#By Using ID
driver.find_element(By.ID, "confirmPassword").send_keys("12345678aA")
time.sleep(5)

#By Using Class Name
driver.find_element(By.CLASS_NAME, "btn").click()
time.sleep(5)