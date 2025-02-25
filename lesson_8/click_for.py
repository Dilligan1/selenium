import time
from logging import exception

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/status_codes")
elements_link = driver.find_elements("tag name","a")
time.sleep(3)
if not elements_link:
    print("Элементы не найдены")
else:
    for click_elements in elements_link:
        try:
            click_elements.click()
            time.sleep(2)
            driver.back()
            time.sleep(2)
        except Exception as e:
            print(f"Ошибка при клике: {e}")