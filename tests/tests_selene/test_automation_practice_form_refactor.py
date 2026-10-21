from selene.core.condition import not_
import time
from datetime import date
import pytest
from selene import browser, be, have, command


class RegistrationPage:

    def window_width(self, value):
        browser.config.window_width = value

    def window_height(self, value):
        browser.config.window_height = value

    def open(self, value):
        browser.open(value)
        # remove google ads
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_phone(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()


def test_submit_form():
    registration_page = RegistrationPage()

    # set windows size
    registration_page.window_width(1920)
    registration_page.window_height(1080)

    # open registration page
    registration_page.open('https://demoqa.com/automation-practice-form')

    # WHEN
    registration_page.fill_first_name('John')  # Заполняем First Name
    registration_page.fill_last_name('Do')  # Заполняем Last Name

    registration_page.fill_user_email('john_do@example.com')  # Заполняем Email
    registration_page.fill_gender('Male')  # Заполняем пол

    registration_page.fill_phone('8566582554')  # Заполняем телефон

    registration_page.fill_date_of_birth('1999', 'May', '11')  # Заполняем дату рождения

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
    browser.element(
        '//div[contains(@class, "subjects-auto-complete__multi-value__label") and text()="History"]').should(
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
    browser.element("#currentAddress").send_keys(
        "Priya Sharma Flat 4B, Sunrise Residency 12 Nehru Nagar, Andheri West Mumbai, Maharashtra 400058")

    # Заполняем State
    browser.element("#react-select-3-input").click().type('N')
    browser.element("#react-select-3-option-3").click()

    # Заполняем City
    browser.element("#react-select-4-input").click()
    browser.element("#react-select-4-option-1").click()

    # Отправлям форму Submit
    browser.element("#submit").click()

    #
    # #Можно проверить заполнение в таблице после отправки
    # browser.all('.table-responsive td:nth-child(2)').should(have.text(
    #     'John',
    #     'Do',
    #     'john_do@example.com'
    #     .......................
    #     итд
    # ))

    time.sleep(2)

    browser.close()
