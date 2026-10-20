from selene.core.condition import not_
import time
from datetime import date
import pytest
from selene import browser, be, have



# Вариант 1
def test_submit_form():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('[placeholder="First Name"]').type("John")  # Заполняем First Name
    browser.element('[placeholder="Last Name"]').type("Do")  # Заполняем Last Name
    browser.element('[placeholder="name@example.com"]').type("john_do@example.com")  # Заполняем Email
    browser.element('[id="gender-radio-1"]').click()  # Заполняем пол
    browser.element('[placeholder="Mobile Number"]').type('8566582554')  # Заполняем телефон
    # Заполняем дату рождения
    # 1. Открываем календарь кликом по полю
    browser.element("#dateOfBirthInput").click()

    # 2. Ждём, пока виджет календаря появится (используем класс из react-datepicker)
    browser.element(".react-datepicker").should(be.visible)

    # 3. Выбираем год (если нужно изменить)
    # В react-datepicker это выпадающий список <select>
    browser.element('[class="react-datepicker__month-container"]').should(be.visible)

    browser.element('.react-datepicker__year-select option[value="1998"]').click()

    # 4. Выбираем месяц (если нужно изменить)
    browser.element('.react-datepicker__month-select option[value="4"]').click()

    # 5. Кликаем по нужному дню
    # Класс дня формируется как: react-datepicker__day--0 + день (с ведущим нулём)
    browser.element(".react-datepicker__day--020").click()

    # Заполняем предмет. В итоге остаются Arts, English, Maths, History
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-2"]').click()
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-1"]').click()
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-3"]').click()
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-4"]').click()
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-5"]').click()
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-6"]').click()
    browser.element('[id="subjectsInput"]').type('C')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-7"]').click()
    browser.element('[aria-label="Remove Computer Science"]').click()
    browser.element('[aria-label="Remove Accounting"]').click()
    browser.element('[aria-label="Remove Physics"]').click()
    browser.element('[id="subjectsInput"]').type('R')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-3"]').click()
    browser.element('[aria-label="Remove Commerce"]').click()
    browser.element('[aria-label="Remove Chemistry"]').click()
    browser.element('[aria-label="Remove Economics"]').click()
    browser.element('[aria-label="Remove Social Studies"]').click()
    browser.element('[aria-label="Remove Civics"]').click()
    browser.element('[id="subjectsInput"]').type('En')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('[id="subjectsInput"]').type('Maths')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-0"]').click()
    browser.element('[id="subjectsInput"]').type('st')
    browser.element('[id="react-select-2-listbox"]').should(be.visible)
    browser.element('[id="react-select-2-option-2"]').click()
    browser.element('//div[contains(@class, "subjects-auto-complete__multi-value__label") and text()="Arts"]').should(
        be.visible)
    browser.element(
        '//div[contains(@class, "subjects-auto-complete__multi-value__label") and text()="English"]').should(
        be.visible)
    browser.element('//div[contains(@class, "subjects-auto-complete__multi-value__label") and text()="Maths"]').should(
        be.visible)
    browser.element('//div[contains(@class, "subjects-auto-complete__multi-value__label") and text()="History"]').should(
        be.visible)

    # Заполняем Hobbies
    # Кликаем по чекбоксу Sports
    browser.element("#hobbies-checkbox-1").click()
    # Проверяем, что он выбран
    browser.element("#hobbies-checkbox-1").should(have.attribute("checked"))

    # Кликаем по чекбоксу Reading
    browser.element("#hobbies-checkbox-2").click()
    # Проверяем, что он выбран
    browser.element("#hobbies-checkbox-2").should(have.attribute("checked"))

    # Кликаем по чекбоксу Music
    browser.element("#hobbies-checkbox-3").click()
    # Проверяем, что он выбран
    browser.element("#hobbies-checkbox-3").should(have.attribute("checked"))

    # Выключаем Sports
    browser.element("#hobbies-checkbox-1").click()
    # Проверяем, что он невыбран
    browser.element("#hobbies-checkbox-1").should(not_(have.attribute("checked")))

    # Выключаем Music
    browser.element("#hobbies-checkbox-3").click()
    # Проверяем, что он невыбран
    browser.element("#hobbies-checkbox-3").should(not_(have.attribute("checked")))

    # Выключаем Reading
    browser.element("#hobbies-checkbox-2").click()
    # Проверяем, что он невыбран
    browser.element("#hobbies-checkbox-2").should(not_(have.attribute("checked")))

    # Кликаем по чекбоксу Reading
    browser.element("#hobbies-checkbox-2").click()
    # Проверяем, что он выбран
    browser.element("#hobbies-checkbox-2").should(have.attribute("checked"))

    # Кликаем по чекбоксу Sports
    browser.element("#hobbies-checkbox-1").click()
    # Проверяем, что он выбран
    browser.element("#hobbies-checkbox-1").should(have.attribute("checked"))

    # Прикрепляем файл
    browser.element("#uploadPicture").send_keys(r"C:\Users\Yo\PycharmProjects\PythonProject\image.png")

    # Вводим текущий адрес
    browser.element("#currentAddress").send_keys("Priya Sharma Flat 4B, Sunrise Residency 12 Nehru Nagar, Andheri West Mumbai, Maharashtra 400058")

    # Заполняем State
    browser.element("#react-select-3-input").click().type('N')
    browser.element("#react-select-3-option-3").click()

    # Заполняем City
    browser.element("#react-select-4-input").click()
    browser.element("#react-select-4-option-1").click()

    # Отправлям форму Submit
    browser.element("#submit").click()

    time.sleep(2)

    browser.close()
