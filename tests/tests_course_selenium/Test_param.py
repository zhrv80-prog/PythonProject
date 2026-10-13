from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest
import math

print("СТАРТ СКРИПТА")

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url1', [
    "https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"
    ])
def test_param(browser, url1):
    #авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
   
    #Открыть страницу 
    try:
        link = url1
        browser = webdriver.Chrome()
        browser.get(link)

        time.sleep(10)
        #Нажимаем на ссылку "Войти"
        element = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
        element.click()

        # ждем загрузки страницы
        time.sleep(20)

        #авторизоваться со своими логином и паролем 
        #Заполняем логин и пароль
        input1 = browser.find_element(By.CSS_SELECTOR, ".ember-text-field.ember-view.sign-form__input[name='login']")
        input1.send_keys("zhrv80@gmail.com")
        input2 = browser.find_element(By.CSS_SELECTOR, ".ember-text-field.ember-view.sign-form__input[name='password']")
        input2.send_keys("")

        time.sleep(2)
        #Нажимаем кнопку "Войти"
        button1 = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader[type='submit']")
        button1.click()

        #дождаться того, что поп-апа с авторизацией больше нет
        time.sleep(10)

        answer = math.log(int(time.time()))

        #ввести правильный ответ (поле перед вводом должно быть пустым)
        #wait = WebDriverWait(browser, 10)
        #element2 = wait.until(
        #   EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea"))
        #  )
        
        element2 = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
        #print('ЕЛЕМЕНТ НАЙДЕН')
        #time.sleep(20)
        #print("\n✅ Элемент найден по селектору!")
        #print(f"Видим: {element2.is_displayed()}")
        #print(f"Доступен: {element2.is_enabled()}")
        #element2.clear()
        element2.send_keys(answer)

        time.sleep(10)

        #нажать кнопку "Отправить" 
        button2 = browser.find_element(By.CSS_SELECTOR, ".submit-submission[type='button']")
        button2.click()

        #дождаться фидбека о том, что ответ правильный 
        time.sleep(10)

        text1 = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert text1.text == "Correct!"
        if text1.text != "Correct!":
            print(text1.text)

        #Нажимаем кнопку "Решить снова"
        #button3 = browser.find_element(By.CSS_SELECTOR, "")
        #button3.click()
        #проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


