from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import math

#авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
#открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
#Открыть страницу 
link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(10)
#Нажимаем на ссылку "Войти"
element = browser.find_element(By.CSS_SELECTOR, ".ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button[href='/lesson/236895/step/1?auth=login']")
element.click()

# ждем загрузки страницы
time.sleep(20)

#авторизоваться со своими логином и паролем 
#Заполняем логин и пароль
input1 = browser.find_element(By.CSS_SELECTOR, ".ember-text-field.ember-view.sign-form__input[name='login']")
input1.send_keys("")
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
element2 = browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")
element2.clear()
element2.send_keys(answer)

#нажать кнопку "Отправить" 
button2 = browser.find_element(By.CSS_SELECTOR, ".submit-submission[type='button']")
button2.click()

#дождаться фидбека о том, что ответ правильный 
time.sleep(10)

#проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"