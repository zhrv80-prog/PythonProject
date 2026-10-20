from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

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

#Заполняем логин и пароль
input1 = browser.find_element(By.CSS_SELECTOR, ".ember-text-field.ember-view.sign-form__input[name='login']")
input1.send_keys("")
input2 = browser.find_element(By.CSS_SELECTOR, ".ember-text-field.ember-view.sign-form__input[name='password']")
input2.send_keys("")

time.sleep(2)
#Нажимаем кнопку "Войти"
button1 = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader[type='submit']")
button1.click()

time.sleep(10)
#авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
#открыть в Chrome урок по ссылке https://stepik.org/lesson/236895/step/1
#авторизоваться со своими логином и паролем 
#дождаться того, что поп-апа с авторизацией больше нет
#ввести правильный ответ (поле перед вводом должно быть пустым)
#нажать кнопку "Отправить" 
#дождаться фидбека о том, что ответ правильный 
#проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"