import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

driver.get("https://www.demoblaze.com/")
iMG_CLICK =("xpath","//img[@class ='card-img-top img-fluid']")
driver.find_element(*iMG_CLICK).click()