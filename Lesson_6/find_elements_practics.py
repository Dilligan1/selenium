import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# driver.get("https://habr.com/ru/articles/")
# elements = driver.find_elements("class name","tm-main-menu__item")
# if not elements:
#     print("Элементы не найдены")
# else:
#     for click_elements in elements:
#         try:
#             click_elements.click()
#             time.sleep(2)
#         except Exception as e:
#             print(f"Ошибка при клике: {e}")
#     # driver.find_elements("class name","tm-main-menu__item")[6].click()
#     time.sleep(5)
#
#

driver.get("https://www.google.ru/")
time.sleep(3)
elements_google = driver.find_elements("class name","KxwPGc SSwjIe")
if not elements_google:
    print(f'К сожалению, на странице нет этих элементов {elements_google}')
    for element_go in elements_google:
        try:
            element_go.click()
            time.sleep(2)
        except Exception as e:
             print(f"Ошибка при клике: {e}")


