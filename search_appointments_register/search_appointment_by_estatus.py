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
    
    # Відкрити випадаючий список "статус обробки за програмою eHealth"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_eh_program_processing_status-container')
    selectBtn.click()
    time.sleep(1)
    
    # Пошук по значенню "Новий"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_eh_program_processing_status-results')
    selectOption = selectDropdown.find_element(By.CSS_SELECTOR, 'li')
    selectOption.click()
    time.sleep(1)
    
    # Натиснути на кнопку "Пошук"
    searchBtn = browser.find_element(By.CSS_SELECTOR, 'button[title="Застосувати фільтри"]')
    searchBtn.click()
    

finally:
    time.sleep(5)
    browser.quit()
    