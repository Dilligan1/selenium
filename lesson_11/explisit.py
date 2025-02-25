import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,10, poll_frequency=1)



# VISIBLE_AFFTER_LINK = ("xpath","//img[@class ='card-img-top img-fluid']")
# driver.get("https://www.demoblaze.com/")
# BUTTON_CLICK = wait.until(EC.visibility_of_element_located(VISIBLE_AFFTER_LINK))
# BUTTON_CLICK.click()
#
# ENABLE_IN_SECONDS = ("xpath", "//img[@class ='card-img-top img-fluid']")
# ENABLE_CLIC = wait.until(EC.element_to_be_clickable(ENABLE_IN_SECONDS))
# ENABLE_CLIC.click()


driver.get('https://the-internet.herokuapp.com/dynamic_controls')
# REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
# driver.find_element(*REMOVE_BUTTON).click()
#
# wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON))
# print('ВСЕ ОК')

ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
TEXT_FIELD = ("xpath", "//input[@type='text']")

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys('Проверочка')
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD,'Проверочка'))
time.sleep(5)
print('Все ок')