from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    browser = webdriver.Chrome()
    link = "https://doctor.stage-health.mia.software/"
    browser.get(link)
    browser.maximize_window()
    
    # Створення епізоду в рамках прийому з мінімальним набором даних
    
    # Блок авторизації
    loginField = browser.find_element(By.CSS_SELECTOR, "input#id_login")
    loginField.send_keys("bloodyhandedreaver@gmail.com")
    
    passwordField = browser.find_element(By.CSS_SELECTOR, "input#id_password")
    passwordField.send_keys("123")
    
    authButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    authButton.click()
    
    # Створення прийому
    # Натиснути на пункт меню "Записи на прийом"
    appointmentRecordLink = browser.find_element(By.CSS_SELECTOR, 'a[href="/appointment/"]')
    appointmentRecordLink.click()
    # Натиснути на кнопку "Додати"
    createAppointmentButton = browser.find_element(By.CSS_SELECTOR, 'button#add-appointment')
    createAppointmentButton.click()
    
    time.sleep(1)
    
    # Пошук пацієнта за ПІБ 
    # Відкрити вкладку "ПІБ"
    patientFullNameTab = browser.find_element(By.CSS_SELECTOR, 'a[href="#fullName"]')
    patientFullNameTab.click()
    
    time.sleep(1)
    
    # Заповнити поля 
    patientLastNameInput = browser.find_element(By.CSS_SELECTOR, "input#id_search_last_name")
    patientLastNameInput.send_keys("Голуб")
    
    patientFirstNameInput = browser.find_element(By.CSS_SELECTOR, "input#id_search_first_name")
    patientFirstNameInput.send_keys("Олександр")
    
    patientMiddleNameInput = browser.find_element(By.CSS_SELECTOR, "input#id_search_middle_name")
    patientMiddleNameInput.send_keys("Анатолійович")
    
    patientBirthDateInput = browser.find_element(By.CSS_SELECTOR, "input#id_search_birthday")
    patientBirthDateInput.send_keys("04.04.1989")
    
    patientSearchButton = browser.find_element(By.CSS_SELECTOR, 'button#fullNameSearch')
    patientSearchButton.click()
    
    time.sleep(1)
    
    # Вибір пацієнта
    table = browser.find_element(By.CSS_SELECTOR, '#fullNameSearchPatientList')
    selectPatientButtons = table.find_elements(By.CSS_SELECTOR, 'button')
    selectPatientButtons[1].click()
    time.sleep(1)
    
    # Перехід до розкладу
    nextStepButton = browser.find_element(By.CSS_SELECTOR, 'button[name="_save"]')
    nextStepButton.click()
    time.sleep(1)
    
    # Вибрати спеціальність
    specializationSelect = browser.find_element(By.CSS_SELECTOR, '#select2-id_specialization-container')
    specializationSelect.click()
    time.sleep(1)
    
    specializationDropdown = browser.find_element(By.CSS_SELECTOR, 'select2-dropdown')
    specializationSearch = specializationDropdown.find_element(By.CSS_SELECTOR, 'input.select2-search__field')
    specializationSearch.send_keys("Терапевт")
    
    selectOption = specializationDropdown.find_element(By.CSS_SELECTOR, 'li.select2-results__option')
    selectOption.click()
    
    # Вибрати лікаря
    doctorSelect = browser.find_element(By.CSS_SELECTOR, '#select2-id_doctor-container')
    doctorSelect.click()
    time.sleep(1)
    
    doctorDropdown = browser.find_element(By.CSS_SELECTOR, 'ul.select2-results__options')
    doctorSearch = doctorDropdown.find_element(By.CSS_SELECTOR, 'input.select2-search__field')
    doctorSearch.send_keys("Анякін")
    
    doctorOption = browser.find_element(By.CSS_SELECTOR, 'li.select2-results__option')
    selectOption.click()
    time.sleep(1)
    
    # Обрати час
    scheduleTable = browser.find_element(By.CSS_SELECTOR, 'div#schedule-container')
    freeTimeArray = browser.find_elements(By.CSS_SELECTOR, 'label.med-time-free')
    freeTimeArray[0].click()
    nextStepButton = browser.find_element(By.CSS_SELECTOR, 'button[name="_save"]')
    nextStepButton.click()
    time.sleep(1)
    
    # Вибір лікаря
    nextStepButton = browser.find_element(By.CSS_SELECTOR, 'button[name="_save"]')
    nextStepButton.click()
    time.sleep(1)
    
    # Розклад лікаря (Мета прийому)
    nextStepButton = browser.find_element(By.CSS_SELECTOR, 'button[name="_save"]')
    nextStepButton.click()
    time.sleep(1)
    
    # Запис на прийом
    closeModalButton = browser.find_element(By.CSS_SELECTOR, 'button[data-dismiss="modal"]')
    closeModalButton.click()
    time.sleep(1)
    
    # Обрати прийом
    appointmentTable = browser.find_element(By.CSS_SELECTOR, 'table#result_list')
    appointments = appointmentTable.find_elements(By.CSS_SELECTOR, 'tr')
    appointmentLink = appointments[1].find_element(By.CSS_SELECTOR, 'a')
    appointmentLink.click()
    time.sleep(1)
    
    # Розпочати прийом
    startAppointment = browser.find_element(By.CSS_SELECTOR, 'a.add-appointment')
    startAppointment.click()
    time.sleep(5)
    
    # Перейти на вкладку епізоди
    episodeTab = browser.find_element(By.CSS_SELECTOR, 'a[href="#episode-combined"]')
    episodeTab.click()
    time.sleep(1)
    
    # Додати епізод
    episodeAddBtn = browser.find_element(By.CSS_SELECTOR, 'button#id_add_episode_combined')
    episodeAddBtn.click()
    time.sleep(1)
    
    # __________________________________________________
    
    # Додати діагноз (натиснути на кнопку)
    episodeSectionArray = browser.find_elements(By.CSS_SELECTOR, 'div.border-bottom-grey')
    diagnosCreateBtn = episodeSectionArray[3].find_element(By.CSS_SELECTOR, 'div.dropdown')
    diagnosCreateBtn.click()
    time.sleep(1)
    
    # Додати діагноз (вибрати варіант)
    diagnosDropdown = episodeSectionArray[3].find_element(By.CSS_SELECTOR, 'ul.dropdown-menu')
    diagnosOption = diagnosDropdown.find_element(By.XPATH, '//a[contains(text(), "Новий")]')
    diagnosOption.click()
    time.sleep(1)
    
    # Модальне вікно "Додати діагноз", поле "МКХ-10-АМ"
    diagnosModal = browser.find_element(By.CSS_SELECTOR, 'div.med-patient-modal')
    diagnosSelect = diagnosModal.find_element(By.CSS_SELECTOR, '#select2-id_disease_am-container')
    diagnosSelect.click()
    time.sleep(1)
    
    # Модальне вікно "Додати діагноз", ввод даних у поле "МКХ-10-АМ"
    diagnosDropdown = browser.find_element(By.CSS_SELECTOR, 'span.select2-dropdown')
    diagnosSearch = diagnosDropdown.find_element(By.CSS_SELECTOR, 'input.select2-search__field')
    diagnosSearch.send_keys("Бронхіт та пневмоніт")
    diagnosOption = diagnosDropdown.find_element(By.CSS_SELECTOR, 'li.select2-results__option')
    diagnosOption.click()
    
    # Збереження
    nextStepButton = browser.find_element(By.CSS_SELECTOR, 'button[name="_save"]')
    nextStepButton.click()
    time.sleep(1)
    
    # __________________________________________________
    
    # Додати направлення на лікування (натиснути на кнопку)
    episodeSectionArray = browser.find_elements(By.CSS_SELECTOR, 'div.border-bottom-grey')
    appointmentCreateBtn = episodeSectionArray[7].find_element(By.CSS_SELECTOR, 'div.dropdown')
    appointmentCreateBtn.click()
    time.sleep(1)
    
    # Додати направлення на лікування (вибрати варіант)
    appointmentDropdown = episodeSectionArray[7].find_element(By.CSS_SELECTOR, 'ul.dropdown-menu')
    createHealAppointment = appointmentDropdown.find_element(By.XPATH, '//a[contains(text(), "Направлення на лікування")]')
    createHealAppointment.click()
    time.sleep(1)
    
    # Вибрати лікаря
    appointmentDoctorRow = browser.find_element(By.CSS_SELECTOR, 'div.specialization_input')
    appointmentDoctorSelect = appointmentDoctorRow.find_element(By.CSS_SELECTOR, 'span.selection')
    appointmentDoctorSelect.click()
    time.sleep(1)
    
    appointmentDoctorDropdown = browser.find_element(By.CSS_SELECTOR, 'ul.select2-results__options')
    appointmentDoctorOptions = appointmentDoctorDropdown.find_elements(By.CSS_SELECTOR, 'li')
    appointmentDoctorOptions[17].click()
    time.sleep(1)
    
    nextStepButton = browser.find_element(By.CSS_SELECTOR, 'button[name="_save"]')
    nextStepButton.click()
    time.sleep(1) 
    
    # __________________________________________________
    
    # Додати дію (Відкрити модальне вікно)
    episodeSectionArray = browser.find_elements(By.CSS_SELECTOR, 'div.border-bottom-grey')
    actionCreateBtn = episodeSectionArray[16].find_element(By.CSS_SELECTOR, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", actionCreateBtn)
    actionCreateBtn.click()
    time.sleep(1)
    
    # Додати дію (Вибрати варіант)
    addActionBtn = browser.find_element(By.CSS_SELECTOR, 'a#formset-add-ehealth-services')
    addActionBtn.click()
    time.sleep(1)
    
    # Обрати код / назву дії
    actionNameSelect = browser.find_element(By.CSS_SELECTOR, 'span.select2-selection__rendered')
    actionNameSelect.click()
    time.sleep(1)
    
    actionNameDropdown = browser.find_element(By.CSS_SELECTOR, 'ul.select2-results__options')
    actionNameOptions = actionNameDropdown.find_elements(By.CSS_SELECTOR, 'li')
    actionNameOptions[2].click()
    time.sleep(1)
    
    nextStepBtn = browser.find_element(By.CSS_SELECTOR, 'button[name="_save"]')
    nextStepBtn.click()
    time.sleep(1)
    
    # Збереження епізоду
    saveEpisodeBtn = browser.find_element(By.CSS_SELECTOR, 'button#save-button')
    saveEpisodeBtn.click()
    time.sleep(1)
    
    # Завершення прийому
    endAppointmentBtn = browser.find_element(By.CSS_SELECTOR, 'button#submit_button')
    endAppointmentBtn.click()
    
    # Підписання прийому (натиснути на кнопку)
    signBtn = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Підписати")]'))
    )
    signBtn.click()
    
    # Підписання прийому (модальне вікно)
    signModal = browser.find_element(By.CSS_SELECTOR, 'div.sign-container')
    
    # Завантажити файловий ключ
    apkInput = signModal.find_element(By.CSS_SELECTOR, 'div.sign-container')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'pb_3527815859.jks') 
    apkInput.send_keys(file_path)
    
    # Ввести пароль
    apkPassword = signModal.find_element(By.CSS_SELECTOR, 'input#pKeyPassword')
    apkPassword.send_keys("AllseeingEYE0")
    
    readKeyBtn = signModal.find_element(By.CSS_SELECTOR, 'button#sign-button')
    readKeyBtn.click()
    
    # Підтвердити
    applyBtn = browser.find_element(By.CSS_SELECTOR, 'button#apply-button')
    applyBtn.click()
    time.sleep(1)
    
    # Перейти до результатів прийому
    appointmentResultBtn = browser.find_element(By.CSS_SELECTOR, 'button#appointment-result-button')
    appointmentResultBtn.click()
    
    # Закрити
    closeResultBtn = browser.find_element(By.XPATH, '//a[contains(text(), "Закрити")]')
    closeResultBtn.click()

finally:
    time.sleep(10)
    browser.quit()
    