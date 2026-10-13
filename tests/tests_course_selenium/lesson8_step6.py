from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.by import By

import math  # Импорт math для математических функций

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

#Открыть страницу https://SunInJuly.github.io/execute_script.html.
link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    print(x)
    
    #Посчитать математическую функцию от x.
    y = calc(x)
    
    #Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 100);")
    
    #Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    #Выбрать checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    
    #Переключить radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    
    #Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()  

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


