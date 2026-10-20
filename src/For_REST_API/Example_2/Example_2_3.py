#Домашнее задание №7: Запросы и методы
"""
Скрипт для проверки API compare_query_type.

Проверяет:
1. Запрос без параметра method
2. Запрос методом не из списка (HEAD)
3. Запрос с правильным method
4. Все комбинации HTTP-метода и параметра method
"""
import requests

URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"
METHODS = ["GET", "POST", "PUT", "DELETE"]


def step_1_no_method():
    """Шаг 1: запрос без параметра method."""
    print("=" * 60)
    print("ШАГ 1: Запрос без параметра method")
    print("=" * 60)

    response = requests.get(URL, timeout=5)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.text}")
    print()


def step_2_wrong_method():
    """Шаг 2: запрос методом не из списка (HEAD)."""
    print("=" * 60)
    print("ШАГ 2: Запрос методом HEAD")
    print("=" * 60)

    response = requests.head(URL, timeout=5)
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.text!r}")  # !r — показать repr
    print()


def step_3_correct_method():
    """Шаг 3: запрос с правильным method."""
    print("=" * 60)
    print("ШАГ 3: Запрос с правильным method")
    print("=" * 60)

    response = requests.get(
        URL,
        params={"method": "GET"},
        timeout=5,
    )
    print(f"Статус: {response.status_code}")
    print(f"Ответ: {response.text}")
    print()


def step_4_all_combinations():
    """Шаг 4: все комбинации HTTP-метода и параметра method."""
    print("=" * 60)
    print("ШАГ 4: Все комбинации")
    print("=" * 60)

    print(f"{'HTTP':<8} {'method':<8} {'Совпадение':<12} {'Ответ':<30}")
    print("-" * 60)

    for http_method in METHODS:
        for param_method in METHODS:
            # Получаем функцию requests по имени
            request_func = getattr(requests, http_method.lower())

            response = request_func(
                URL,
                params={"method": param_method},
                timeout=5,
            )

            is_match = http_method == param_method
            is_success = "success" in response.text.lower()

            # Отмечаем несоответствия
            mark = ""
            if is_match != is_success:
                mark = "!!!!"

            print(
                f"{http_method:<8} {param_method:<8} "
                f"{str(is_match):<12} {response.text[:30]:<30}{mark}"
            )

    print()


def main():
    """Запускает все шаги."""
    step_1_no_method()
    step_2_wrong_method()
    step_3_correct_method()
    step_4_all_combinations()


if __name__ == "__main__":
    main()