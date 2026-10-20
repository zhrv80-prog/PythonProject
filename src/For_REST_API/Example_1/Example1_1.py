import requests


def main():
    """Отправляет GET-запрос и выводит текст ответа."""
    url = "https://playground.learnqa.ru/api/get_text"
    response = requests.get(url, timeout=5)
    print(response.text)


if __name__ == "__main__":
    main()