import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')   # для CI-сервера без GUI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_page_title(driver):
    driver.get('http://localhost:5000')
    assert 'CI/CD Demo' in driver.title

def test_form_submission_with_name(driver):
    driver.get('http://localhost:5000')
    name_input = driver.find_element(By.NAME, 'username')
    name_input.send_keys('Иван')
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()
    greeting = driver.find_element(By.TAG_NAME, 'h3').text
    assert 'Привет, Иван!' in greeting

def test_empty_name_submission(driver):
    driver.get('http://localhost:5000')
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()
    # Поле required, браузер покажет всплывающую подсказку, страница не перезагрузится
    # Проверяем, что приветствие отсутствует
    h3_elements = driver.find_elements(By.TAG_NAME, 'h3')
    assert len(h3_elements) == 0

def test_button_exists(driver):
    driver.get('http://localhost:5000')
    button = driver.find_element(By.TAG_NAME, 'button')
    assert button.is_displayed()
    assert button.text == 'Отправить'