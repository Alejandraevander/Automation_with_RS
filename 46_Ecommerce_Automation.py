from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count>=3

for result in results:
    result.find_element(By.XPATH,"div/button").click()
    time.sleep(3)
    
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()
driver.implicitly_wait(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)