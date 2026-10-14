"""
Скрипт для тестирования API longtime_job.

1. Создаёт задачу
2. Проверяет, что задача ещё не готова
3. Ждёт нужное количество секунд
4. Проверяет, что задача готова и есть результат
"""
import time
import requests

URL = "https://playground.learnqa.ru/ajax/api/longtime_job"


def main():
    """Основная функция скрипта."""

    # ===== ШАГ 1: Создаём задачу =====
    print("=" * 60)
    print("ШАГ 1: Создаём задачу")
    print("=" * 60)

    response = requests.get(URL, timeout=5)
    data = response.json()

    print(f"Ответ: {data}")

    seconds = data["seconds"]
    token = data["token"]

    print(f"  Задача будет готова через {seconds} секунд")
    print(f" Token: {token}")
    print()

    # ===== ШАГ 2: Проверяем ДО готовности =====
    print("=" * 60)
    print("ШАГ 2: Проверяем ДО готовности")
    print("=" * 60)

    response = requests.get(
        URL,
        params={"token": token},
        timeout=5,
    )
    data = response.json()

    print(f"Ответ: {data}")

    assert data["status"] == "Job is NOT ready", (
        f"Ожидался 'Job is NOT ready', получен: {data['status']}"
    )
    assert "result" not in data, "Поле 'result' не должно быть!"

    print(" Задача ещё не готова — правильно!")
    print()

    # ===== ШАГ 3: Ждём =====
    print("=" * 60)
    print(f"ШАГ 3: Ждём {seconds + 1} секунд")
    print("=" * 60)

    time.sleep(seconds + 1)  #  +1 для надёжности

    print(" Время вышло")
    print()

    # ===== ШАГ 4: Проверяем ПОСЛЕ готовности =====
    print("=" * 60)
    print("ШАГ 4: Проверяем ПОСЛЕ готовности")
    print("=" * 60)

    response = requests.get(
        URL,
        params={"token": token},
        timeout=5,
    )
    data = response.json()

    print(f"Ответ: {data}")

    assert data["status"] == "Job is ready", (
        f"Ожидался 'Job is ready', получен: {data['status']}"
    )
    assert "result" in data, "Поле 'result' должно быть!"

    print(f" Задача готова!")
    print(f" Результат: {data['result']}")
    print()

    print("=" * 60)
    print(" Все проверки пройдены!")
    print("=" * 60)


if __name__ == "__main__":
    main()