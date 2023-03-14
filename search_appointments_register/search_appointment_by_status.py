from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    browser = webdriver.Chrome()
    link = "https://doctor.stage-health.mia.software/"
    browser.get(link)
    browser.maximize_window()
    
    # Блок авторизації
    loginField = browser.find_element(By.CSS_SELECTOR, "input#id_login")
    loginField.send_keys("bloodyhandedreaver@gmail.com")
    
    passwordField = browser.find_element(By.CSS_SELECTOR, "input#id_password")
    passwordField.send_keys("123")
    
    authButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    authButton.click()
    
    # Перехід до реєстру направлень
    registersTitle = browser.find_element(By.CSS_SELECTOR, 'a[href="#registers"]')
    registersTitle.click()
    time.sleep(1)
    
    appointmentRegisterBtn = browser.find_element(By.CSS_SELECTOR, 'a[href="/referral/"]')
    appointmentRegisterBtn.click()
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Чернетка"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[0].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Активний"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[1].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Підписана"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[2].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Відкликаний"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[3].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "В роботі"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[4].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Завершено"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[5].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Введений помилково"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[6].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Частково готове"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[7].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    time.sleep(5)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Статус"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Скасовано"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_status-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[8].click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()

finally:
    time.sleep(5)
    browser.quit()
    