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
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
window_open = driver.window_handles
driver.switch_to.window(window_open[1])
email = driver.find_element(By.XPATH,"//p[@class='im-para red']//strong").text

driver.switch_to.window(window_open[0])
driver.find_element(By.XPATH,"//input[@name='username']").send_keys(email)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("12345678i")
driver.find_element(By.XPATH,"//input[@name='signin']").click()


wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)