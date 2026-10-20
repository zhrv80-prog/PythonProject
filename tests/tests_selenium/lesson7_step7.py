from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    #Находим на ней элемент-картинку, который является изображением сундука с сокровищами.
    x_element = browser.find_element(By.CSS_SELECTOR, "img#treasure[valuex]")
    
    #Берем у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = x_element.get_attribute("valuex")
    
    #Посчитаем математическую функцию от x
    y = calc(x)
    
    #Вводим ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    #Отмечаем checkbox "I'm the robot"
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    
    #Выбираем radiobutton "Robots rule!"
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    
    #Нажимаем на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button")
    button.click()
          
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла




