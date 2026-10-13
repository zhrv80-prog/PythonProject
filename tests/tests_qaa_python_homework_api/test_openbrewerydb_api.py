import time

import pytest
import requests
from jsonschema import validate
import cerberus
import allure

# 5 Тестов из них 2 c параметризацией

#===== ТЕСТ 1: Статус-код =====
def test_openbrewerydb_url_api_response_200(openbrewerydb_url_api):
    """Проверяет что api возвращает 200 """
    url = f"{openbrewerydb_url_api}"
    r = requests.get(url)
    assert r.status_code == 200

#===== ТЕСТ 2: Проверяет тип данных в ответе =====
def test_openbrewerydb_url_api_id_is_string(openbrewerydb_url_api):
    """Проверяет что id, name алкогольного напитка в ответе имеет тип данных string"""

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }

    url = f"{openbrewerydb_url_api}v1/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
    r = requests.get(url, timeout=5)
    print(url)

    data = r.json()
    validate(instance=data, schema=schema)

#===== ТЕСТ 3: Проверяет пагинацию =====
@pytest.mark.parametrize("per_page", [1, 2, 5, 7, 10, 50, 100])
def test_openbrewerydb_url_api_pagination(openbrewerydb_url_api, per_page):
    """Проверяет, что возвращается то количество элементов, которое передано в per_page"""
    url = f"{openbrewerydb_url_api}v1/breweries?per_page={per_page}"
    res = requests.get(url, timeout=5)
    data = res.json()

    assert res.status_code == 200
    assert len(data) == per_page

# ===== ТЕСТ 4: Проверяет время ответа < 2 =====
@pytest.mark.parametrize("url", [
    "https://api.openbrewerydb.org/v1/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
    "https://api.openbrewerydb.org/v1/breweries/random"
], ids=["Single Brewery", "Random Brewery"])
@allure.title("Проверка времени ответа API: {url}")  # 👈 Добавлен заголовок
def test_response_time(url):
    with allure.step("Выполнение GET-запроса"):  # 👈 Шаг 1
        start_time = time.time()
        res = requests.get(url, timeout=50)
        end_time = time.time()

    with allure.step("Вычисление и проверка времени ответа"):  # 👈 Шаг 2
        response_time = end_time - start_time
        print(response_time)
        assert res.status_code == 200
        assert response_time < 2

#===== ТЕСТ 5: Фильтрация по state =====
@pytest.mark.parametrize("state", ["California", "New York", "Utah"], ids=["state = California", "state = New York", "state = Utah"])
@pytest.mark.parametrize("per_page", [1, 2, 5, 7, 10, 50, 100])
def test_openbrewerydb_url_api_filter_by_state(openbrewerydb_url_api, state, per_page):
    """Проверяет что ответ содержит значение штат, переданное в state для разных значений per_page"""
    url = f"{openbrewerydb_url_api}v1/breweries?by_state={state}&per_page={per_page}"
    res = requests.get(url, timeout=5)
    data = res.json()
    #assert res.status_code == 200
    for data in data:
        assert data["state"] == state






