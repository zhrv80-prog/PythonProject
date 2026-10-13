import pytest
import requests
from pyparsing import Char


#===== ТЕСТ 1: Статус-код =====
def test_placeholder_api_status_code(jsonplaceholder_url_api):
    url = jsonplaceholder_url_api
    res = requests.get(url)
    assert res.status_code == 200

#===== ТЕСТ 2: Метод POST =====
def test_placeholder_api_post_request(jsonplaceholder_url_api):
    """Проверяет создание поста через POST."""
    url = f"{jsonplaceholder_url_api}/posts"

    data = {
        "userId": 1,
        "title": "este el titulo de mi solicitud",
        "body": "este mi solicitud"
    }

    headers = {"Content-Type": "application/json; charset=UTF-8"}

    res = requests.post(url, json=data, headers=headers, timeout=5)

    # 1. Статус-код
    assert res.status_code == 201, f"Ожидался 201, получен {res.status_code}"

    # 2. Ответ — JSON
    response_data = res.json()
    assert isinstance(response_data, dict)

    # 3. Сервер присвоил id
    assert "id" in response_data
    assert isinstance(response_data["id"], int)

    # 4. Данные совпадают
    assert response_data["userId"] == data["userId"]
    assert response_data["title"] == data["title"]
    assert response_data["body"] == data["body"]

#===== ТЕСТ 3: Параметр командной строки =====
def test_placeholder_api_get_request_cmdopt(jsonplaceholder_url_api, cmdopt):
    url = f"{jsonplaceholder_url_api}/posts/{cmdopt}"
    res = requests.get(url, timeout=5)

    assert (res.json())["id"] == int(cmdopt)
    assert res.status_code == 200


