from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button1 = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    # Или альтернативные селекторы:
    # button1 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # button1 = browser.find_element(By.CLASS_NAME, "trollface")
    button1.click()

    # Переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    
    # Дать время для загрузки страницы
    time.sleep(1)

    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    # Или: button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
    # Получить результат из alert
    time.sleep(1)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


    