from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_py
import time

service = Service(chromedriver_py.binary_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # Открываем страницу
    driver.get("https://stepik.org/lesson/236895/step/1")
    time.sleep(3)
    
    print("=== ДИАГНОСТИКА СТРАНИЦЫ ===")
    
    # 1. Проверяем iframe
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"1. Найдено iframe на странице: {len(iframes)}")
    
    for i, iframe in enumerate(iframes):
        print(f"   Iframe {i}:")
        print(f"      ID: {iframe.get_attribute('id')}")
        print(f"      Class: {iframe.get_attribute('class')}")
        print(f"      Src: {iframe.get_attribute('src')}")
    
    # 2. Проверяем, есть ли кнопка "Войти"
    try:
        login_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Войти"))
        )
        print("2. ✅ Кнопка 'Войти' найдена")
        print("   Кликаем по ней...")
        login_btn.click()
        time.sleep(2)
    except:
        print("2. ❌ Кнопка 'Войти' не найдена")
    
    # 3. Теперь ищем все textarea на странице
    print("\n3. Поиск всех textarea:")
    
    # Сначала в основном документе
    textareas = driver.find_elements(By.TAG_NAME, "textarea")
    print(f"   Textarea в основном документе: {len(textareas)}")
    
    for i, ta in enumerate(textareas):
        print(f"   Textarea {i}:")
        print(f"      ID: {ta.get_attribute('id')}")
        print(f"      Class: {ta.get_attribute('class')}")
        print(f"      Name: {ta.get_attribute('name')}")
        print(f"      Placeholder: {ta.get_attribute('placeholder')}")
    
    # 4. Проверяем каждый iframe
    if iframes:
        print("\n4. Поиск textarea внутри iframe:")
        for i, iframe in enumerate(iframes):
            driver.switch_to.frame(iframe)
            textareas_in_frame = driver.find_elements(By.TAG_NAME, "textarea")
            print(f"   Iframe {i}: найдено {len(textareas_in_frame)} textarea")
            
            for j, ta in enumerate(textareas_in_frame):
                print(f"      Textarea {j} в iframe {i}:")
                print(f"         Class: {ta.get_attribute('class')}")
                print(f"         ID: {ta.get_attribute('id')}")
            
            driver.switch_to.default_content()
    
    # 5. Если нашли textarea, пробуем с ними работать
    found = False
    
    # Проверяем основной документ
    if textareas and not found:
        print("\n5. Пробуем работать с textarea из основного документа")
        for ta in textareas:
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", ta)
                time.sleep(1)
                ta.clear()
                ta.send_keys("Тестовый текст")
                print(f"✅ Успешно ввели текст в textarea с классом: {ta.get_attribute('class')}")
                found = True
                break
            except Exception as e:
                print(f"❌ Не удалось: {e}")
    
    # Проверяем iframe
    if iframes and not found:
        print("\n6. Пробуем работать с textarea внутри iframe")
        for i, iframe in enumerate(iframes):
            driver.switch_to.frame(iframe)
            textareas_in_frame = driver.find_elements(By.TAG_NAME, "textarea")
            
            for ta in textareas_in_frame:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", ta)
                    time.sleep(1)
                    ta.clear()
                    ta.send_keys("Тестовый текст в iframe")
                    print(f"✅ Успешно ввели текст в textarea в iframe {i}")
                    found = True
                    break
                except Exception as e:
                    print(f"❌ Не удалось в iframe {i}: {e}")
            
            driver.switch_to.default_content()
            if found:
                break
    
    if not found:
        print("\n❌ Не удалось найти ни одной рабочей textarea")
    
except Exception as e:
    print(f"Ошибка: {e}")

finally:
    time.sleep(5)
    driver.quit()