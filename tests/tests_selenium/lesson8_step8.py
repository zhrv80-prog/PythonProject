from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 


#Открыть страницу http://suninjuly.github.io/file_input.html

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
#Заполнить текстовые поля: имя, фамилия, email

    input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    input3.send_keys("Ivanov_Ivan@123mail.com")
    
#Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
#/home/usr/environments

    element = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '123test.txt')        # добавляем к этому пути имя файла 
    element.send_keys(file_path)
    print(os.path.abspath(__file__))

#Нажать кнопку "Submit"

    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


