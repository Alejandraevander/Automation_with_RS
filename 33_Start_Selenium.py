from selenium import webdriver
from selenium.webdriver.edge.service import Service

#Method 1 (Auto Download Driver) - Chrome driver - Chrome Browser
# service_obj = Service()
# driver = webdriver.Edge(service=service_obj)
# driver.get("http://rahulshettyacademy.com")

#Method 2 (Manually Download Driver)
service_obj = Service(r"H:\Python_Project\Section_9_RS_Testing_Framework\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("http://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.back()
driver.forward()
driver.close()