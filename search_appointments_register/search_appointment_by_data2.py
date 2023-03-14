from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import json

@pytest.fixture(scope='session')
def config():
    with open('search_config.json') as config_file:
        data = json.load(config_file)
        return data

try: 
    browser = webdriver.Chrome()
    link = "https://doctor.stage-health.mia.software/"
    browser.get(link)
    browser.maximize_window()
    
    # Блок авторизації
    loginField = browser.find_element(By.CSS_SELECTOR, "input#id_login")
    loginField.send_keys(config['login'])
    
    passwordField = browser.find_element(By.CSS_SELECTOR, "input#id_password")
    passwordField.send_keys(config['password'])
    
    authButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    authButton.click()
    
    # Перехід до реєстру направлень
    registersTitle = browser.find_element(By.CSS_SELECTOR, 'a[href="#registers"]')
    registersTitle.click()
    time.sleep(1)
    
    appointmentRegisterBtn = browser.find_element(By.CSS_SELECTOR, 'a[href="/referral/"]')
    appointmentRegisterBtn.click()
    
    # Відкрити datepicker у колонці "Дата"
    datepickerBtn = browser.find_element(By.CSS_SELECTOR, '#id_created')
    datepickerBtn.click()
    time.sleep(1)
    
    # Пошук актуальної дати
    datepicker = browser.find_element(By.CSS_SELECTOR, 'div.datepicker')
    datepickerDaysTable = datepicker.find_element(By.CSS_SELECTOR, 'div.datepicker-days')
    daysArray = datepickerDaysTable.find_elements(By.CSS_SELECTOR, 'td.day')
    daysArray[23].click()
    daysArray = datepickerDaysTable.find_elements(By.CSS_SELECTOR, 'td.day')
    daysArray[29].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    

finally:
    time.sleep(5)
    browser.quit()
    