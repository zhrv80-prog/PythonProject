#Домашнее задание №6: Длинный редирект
import requests


def main():
    """Отправляет GET-запрос и выводит количество редиректов и итоговый URL."""
    url = "https://playground.learnqa.ru/api/long_redirect"
    response = requests.get(url, timeout=5)

    # Количество редиректов
    number_of_redirects = len(response.history)
    print(f"Количество редиректов: {number_of_redirects}")

    # Итоговый URL
    print(f"Итоговый URL: {response.url}")


if __name__ == "__main__":
    main()