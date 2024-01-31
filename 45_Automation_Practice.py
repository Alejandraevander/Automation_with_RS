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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Checkbox
# check_box = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
# time.sleep(3)

# for check in check_box:
#     if check.get_attribute('value')=="option2":
#         check.click()
#         assert check.is_selected()
#         time.sleep(5)
#         break
    
# #RadioButton
# Radio = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
# Radio[2].click()
# time.sleep(5)

# #Display Box
# assert driver.find_element(By.ID,"displayed-text").is_displayed()
# time.sleep(5)
# driver.find_element(By.ID,"hide-textbox").click()
# time.sleep(5)
# assert not driver.find_element(By.ID,"displayed-text").is_displayed()
# # for radiob in Radio:
# #     if radiob.get_attribute("value") =="radio1":
# #         #radiob.click()
# #         #time.sleep(3)
# #         assert radiob.is_selected()
# #         time.sleep(3)
# #         break

#Alert
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Alejandra")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
time.sleep(5)

#Alert mode
alert = driver.switch_to.alert
print(alert.text)
assert "Alejandra" in alert.text
alert.accept() #OK
#alert.dismiss() #Cancel