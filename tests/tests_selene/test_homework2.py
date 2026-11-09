from datetime import time
import pytest

import this

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=6)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    is_dark_theme = None

    if 6 <= current_time.hour < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


@pytest.mark.parametrize("hour, user_choice, expected_dark", [
    # Пользователь включил вручную — всегда тёмная
    (16, True, True),
    (23, True, True),
    (6, True, True),

    # Пользователь выключил вручную — всегда светлая
    (16, False, False),
    (23, False, False),
    (6, False, False),

    # Пользователь не выбрал (None) — по времени
    (16, None, False),  # День → светлая
    (12, None, False),  # День → светлая
    (23, None, True),  # Ночь → тёмная
    (0, None, True),  # Ночь → тёмная
    (5, None, True),  # Ночь → тёмная
    (6, None, False),  # 06:00 → день (граница)
    (22, None, True),  # 22:00 → ночь (граница)
])
def test_dark_theme_by_time_and_user_choice(hour, user_choice, expected_dark):
    """Проверяет тёмную тему по времени и выбору пользователя."""
    current_time = time(hour=hour)
    dark_theme_enabled_by_user = user_choice

    # Логика
    if dark_theme_enabled_by_user is True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
    else:
        if 6 <= current_time.hour < 22:
            is_dark_theme = False
        else:
            is_dark_theme = True

    assert is_dark_theme is expected_dark, (
        f"Время: {hour}:00, выбор: {user_choice}, "
        f"ожидалось: {expected_dark}, получено: {is_dark_theme}"
    )

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None

    for user in users:
        if user["name"] == "Olga":
            suitable_users = user

    #suitable_users
    print(suitable_users)
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = None
    #suitable_users = [user for user in users if user["age"] < 20]
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)
    print(suitable_users)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def readable_function(func, *args, **kwargs):
    func_name = func.__name__.replace("_", " ").title()
    args_names = ", ".join([*args, *kwargs.values()])
    return f"{func_name} [{args_names}]"


def open_browser(browser_name):
    actual_result = readable_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = readable_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = readable_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


