# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# from Lesson_6.list_practics import elemets
#
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
#
#
# driver.get("https://testautomationpractice.blogspot.com/")
#
# #Поиск иконки по классу
# print(driver.find_element("class name", 'wikipedia-icon'))
#
#
# #Поиск поля ввода по id
# print(driver.find_element("id","Wikipedia1_wikipedia-search-input"))
#
# #Поиск поля поиска по классу
# print(driver.find_element("class name","wikipedia-search-button"))
#
# #Поиск любого тега и вывод его на экран
# elements = driver.find_elements("tag name","div")
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
