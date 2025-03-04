import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/upload')

upload_file = driver.find_element("xpath","//input[@type='file']")
upload_file.send_keys(f"{os.getcwd()}/download_file/example.png")
download_file = driver.find_element("xpath","//input[@id='file-submit']")
download_file.click()
time.sleep(3)