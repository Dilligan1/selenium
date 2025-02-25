import time
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.ru/")


current_title_gl = driver.title
print("Заголовок страницы:", current_title_gl)
sleep(3)
driver.get("https://vk.ru/")
current_title_vk = driver.title
print("Заголовок страницы:", current_title_vk)
driver.back()
assert current_title_gl == 'Google'
time.sleep(3)
driver.refresh()
PAGE_URL = driver.current_url
print(PAGE_URL)
driver.forward()
PAGE_URL = driver.current_url
assert PAGE_URL == "https://vk.ru/"
time.sleep(15)

