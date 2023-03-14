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
    
    # Створити eHealth направлення
    createAppointmentBtn = browser.find_element(By.CSS_SELECTOR, 'a[href="/employee/patient/person/search/?reverse=/referral/"]')
    createAppointmentBtn.click()
    time.sleep(1)
    
    # Пошук пацієнта по мінімальній інформації
    lastNameInput = browser.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
    lastNameInput.send_keys("Карась")
    
    firstNameInput = browser.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
    firstNameInput.send_keys("Євген")
    
    birthDateInput = browser.find_element(By.CSS_SELECTOR, 'input[name="birth_date"]')
    birthDateInput.send_keys("09.08.1979")
    
    patientSearchBtn = browser.find_element(By.CSS_SELECTOR, 'button[name="_search"]')
    patientSearchBtn.click()
    
    # Вибір пацієнта
    patientRow = browser.find_element(By.CSS_SELECTOR, 'div.pv-10')
    createAppointmentBtn = patientRow.find_element(By.CSS_SELECTOR, 'input[name="_match"]')
    createAppointmentBtn.click()
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Категорія"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_category-container')
    selectBtn.click()
    time.sleep(1)
    
    # Ввести значення "Консультація"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_category-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[2].click()
    time.sleep(1)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Пріоритет"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_priority-container')
    selectBtn.click()
    time.sleep(1)
    
    # Ввести значення "Планове"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_priority-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[0].click()
    time.sleep(1)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Послуга"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_eh_service-container')
    selectBtn.click()
    time.sleep(1)
    
    # Знайти необхідне значення
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'span.select2-dropdown')
    selectDropdownSearch = browser.find_element(By.CSS_SELECTOR, 'input.select2-search__field')
    selectDropdownSearch.send_keys("Терапевта")
    time.sleep(1)
    
    # Ввести значення "Планове"
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'span.select2-dropdown')
    selectOption = selectDropdown.find_element(By.CSS_SELECTOR, 'li.select2-results__option--highlighted')
    selectOption.click()
    time.sleep(1)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Епізод"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_episode-container')
    selectBtn.click()
    time.sleep(1)
    
    # Ввести значення
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_episode-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[2].click()
    time.sleep(1)
    
    # __________________________________________________
    
    # Відкрити випадаючий список "Взаємодія"
    selectBtn = browser.find_element(By.CSS_SELECTOR, '#select2-id_visit-container')
    selectBtn.click()
    time.sleep(1)
    
    # Ввести значення
    selectDropdown = browser.find_element(By.CSS_SELECTOR, 'ul#select2-id_visit-results')
    selectOptions = selectDropdown.find_elements(By.CSS_SELECTOR, 'li')
    selectOptions[0].click()
    time.sleep(1)
    
    # __________________________________________________
    
    # Зберегти
    saveBtn = browser.find_element(By.CSS_SELECTOR, 'input[name="_save"]')
    saveBtn.click()

finally:
    time.sleep(10)
    browser.quit()
    