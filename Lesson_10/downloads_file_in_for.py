import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}/download_file"
}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--window-size=1920,1080')
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

download_files = driver.find_elements('xpath','//a')
try:
    download_files = driver.find_elements(By.XPATH, '//a')
    for file in download_files:
        try:
            file.click()
            WebDriverWait(driver, 10).until(EC.staleness_of(file))  # Ожидание обновления страницы
        except Exception as e:
            print(f"Ошибка при клике на ссылку: {e}")
        time.sleep(2)
finally:
    time.sleep(5)
    driver.quit()