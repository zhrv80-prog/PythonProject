import requests

# Создаем GET запрос и выводим его содержимое
def test_get_request():
    res = requests.get("https://playground.learnqa.ru/api/get_text")
    print(res.text)