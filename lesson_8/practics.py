import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")


USER_NAME_FiND = driver.find_element("xpath", "//input[@id = 'userName']")
USER_NAME_FiND.send_keys("dilligan")
time.sleep(2)


USER_EMAIL_FIND = driver.find_element("xpath","//input[@id = 'userEmail']")
USER_EMAIL_FIND.send_keys('dilligan007@mail.ru')
time.sleep(2)

USER_ADRESS_FIND = driver.find_element("xpath","//textarea[@id = 'currentAddress']")
USER_ADRESS_FIND.send_keys("Пухова 56, квартира 119, подъезд 1")
time.sleep(2)

USER_PERMANENTADRESS_FIND = driver.find_element("xpath","//textarea[@id = 'permanentAddress']")
USER_PERMANENTADRESS_FIND.send_keys("Петра Тарасова 17, квартира 95, подъезд 4")
time.sleep(2)

FIND_SUBMIT = driver.find_element("xpath", "//button[@id = 'submit']")
time.sleep(2)
FIND_SUBMIT.click()
time.sleep(3)


# проверки
assert USER_NAME_FiND.get_attribute('value') == "dilligan"
USER_NAME_FiND.clear()
time.sleep(1)
assert USER_EMAIL_FIND.get_attribute('value') == 'dilligan007@mail.ru'
USER_EMAIL_FIND.clear()
time.sleep(1)
assert USER_ADRESS_FIND.get_attribute('value') == "Пухова 56, квартира 119, подъезд 1"
USER_ADRESS_FIND.clear()
time.sleep(1)
assert USER_PERMANENTADRESS_FIND.get_attribute('value') == "Петра Тарасова 17, квартира 95, подъезд 4"
USER_PERMANENTADRESS_FIND.clear()
time.sleep(1)

finaly_testing = driver.find_elements("xpath","//div[contains(@class, 'border')]")
if not finaly_testing:
    print("Элементы не найдены")
else:
    for id_name in finaly_testing:
        atribut = id_name.get_attribute('id')
        print(atribut)

finaly_testing_id = driver.find_elements(By.TAG_NAME, "p")
if not finaly_testing_id:
    print("Элементы не найдены")
else:
    for p in finaly_testing_id:  # исправлено
        print(p.get_attribute("id"))