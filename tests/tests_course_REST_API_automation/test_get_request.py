import json

import requests


# Домашнее задание №4: Создаем GET запрос и выводим его содержимое
def test_get_request():
    res = requests.get("https://playground.learnqa.ru/api/get_text")
    print(res.text)


# Домашнее задание №5: Парсинг JSON
def test_parsing_json():
    json_text = """
    {
      "messages": [
        {
          "message": "This is the first message",
          "timestamp": "2021-06-04 16:40:53"
        },
        {
          "message": "And this is a second message",
          "timestamp": "2021-06-04 16:41:01"
        }
      ]
    }
    """

    data = json.loads(json_text)
    print(data["messages"][1]["message"])
