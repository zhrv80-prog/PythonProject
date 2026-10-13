from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Импортируем класс Select для работы с выпадающими списками
import time 

# Открыть страницу https://suninjuly.github.io/selects1.html
link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    
    # Получаем текст из элементов и преобразуем в числа
    x = int(x_element.text)
    y = int(y_element.text)
    
    z = x + y
    print(f"Сумма чисел: {x} + {y} = {z}")

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    # Используем класс Select для работы с выпадающим списком
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(z))  # Выбираем по значению (value)
    # Альтернативно можно использовать:
    # select.select_by_visible_text(str(z))  # Выбираем по видимому тексту

    # Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
          
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

