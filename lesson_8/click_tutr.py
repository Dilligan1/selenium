import time
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('https://www.freeconferencecall.com/ru')
login_button = driver.find_element("xpath", "//a[@id = 'login-desktop']")
login_button.click()
email_fiend = driver.find_element("xpath", '//input[@class = "form-control login_email"]')
email_fiend.send_keys("dilligan007@mail.ru")
email_fiend.clear()
email_fiend.send_keys("dilli@mail.ru")
# print(email_fiend.get_attribute('value'))
time.sleep(5)