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
    
    # Перехід до розділу "eHealth персони"
    epersonsTitle = browser.find_element(By.CSS_SELECTOR, 'a[href="/person-request/"]')
    epersonsTitle.click()
    time.sleep(1)
    
    # Ввести пошуковий запит
    epersonsSearch = browser.find_element(By.CSS_SELECTOR, 'input[name="search"]')
    epersonsSearch.send_keys("Карась Є.С.")
    
    # Натиснути на кнопку "Пошук"
    epersonsSearchBtn = browser.find_element(By.CSS_SELECTOR, 'a.input-group-addon')
    epersonsSearchBtn.click()

finally:
    time.sleep(10)
    browser.quit()
    