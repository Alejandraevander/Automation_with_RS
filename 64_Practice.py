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
service_obj = Service(r"C:\Users\User\Desktop\Coding_With_RS\edgedriver_win64\msedgedriver.exe")

#Code to disable devtools listening on ....
options_obj.add_experimental_option('excludeSwitches', ['enable-logging'])
#options_obj.add_argument("--headless=new")
#ptions_obj.add_argument("--start-maximized")
#options_obj.add_argument("headless")
#options_obj.add_argument("--ignore-certificate-errors")
options_obj.add_argument("--guest")
options_obj.add_argument("windows-size=1920x1080")

BrowserSortedList =[]
#Initialize Web Driver
driver = webdriver.Edge(service=service_obj, options=options_obj)
driver.implicitly_wait(5)

#Start Calling Website & Program
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.LINK_TEXT,"Shop").click() #//a[contains(@href,'shop')] #a[href*='shop']

Phonelist = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
time.sleep(3)
for Phone in Phonelist:
    P_phone = Phone.find_element(By.XPATH,"div/h4/a").text
    time.sleep(3)
    if P_phone == "Blackberry":
        Phone.find_element(By.XPATH,"div/button").click()
        
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class = 'btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successtext = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success!" in successtext
time.sleep(5)   