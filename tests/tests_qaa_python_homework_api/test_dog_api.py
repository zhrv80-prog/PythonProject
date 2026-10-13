import requests
import pytest
from jsonschema import validate


# ===== ТЕСТ 1: Статус-код. =====
@pytest.mark.parametrize("breed_name", ["affenpinscher", "collie", "dingo"])
def test_dog_api_status_code(dog_url_api, breed_name):
    """Проверяет, что API возвращает 200 для разных пород."""
    url = f"{dog_url_api}/breed/{breed_name}/images"
    r = requests.get(url, timeout=5)

    assert r.status_code == 200, f"URL: {url}, статус: {r.status_code}"


# ===== ТЕСТ 2: Структура JSON. =====
def test_dog_api_response_schema(dog_url_api):
    """Проверяем структуру JSON ответа."""
    schema = {
        "message": [
            "afghan",
            "basset",
            "blood",
            # "english",
            "ibizan",
            "plott",
            # "walker"
        ],
        "status": "success"
    }
    url = f"{dog_url_api}/breed/hound/list"
    r = requests.get(url, timeout=5)
    data = r.json()
    validate(instance=data, schema=schema)


# ===== ТЕСТ 3: Содержимое ответа. =====
@pytest.mark.parametrize("breed_name", ["hound", "shiba"])
def test_dog_api_images_urls(dog_url_api, breed_name):
    """Проверяет что URL картинок корректные."""
    url = f"{dog_url_api}/breed/{breed_name}/images"
    r = requests.get(url, timeout=5)
    images = r.json()["message"]

    print(images)

    assert len(images) > 0, "Список картинок пуст"
    for image_url in images:
        assert image_url.startswith("https://"), f"{image_url} некорректный URL"
        assert image_url.endswith((".jpg", ".jpeg", ".png")), f"{image_url} некорректное расширение"


# ===== ТЕСТ 4: Заголовки. =====
@pytest.mark.parametrize("breed_name", ["mix", "akita"])
def test_dog_api_content_type(dog_url_api, breed_name):
    """Проверяет Content-type ответа."""
    url = f"{dog_url_api}/breed/{breed_name}/images"
    r = requests.get(url, timeout=5)

    assert "application/json" in r.headers["Content-Type"]


# ===== ТЕСТ 5: Обработка ошибок. =====
def test_dog_api_ivalid_breed_name_return_404(dog_url_api):
    """Проверяет, что несуществующая порода возвращает 404."""
    url = f"{dog_url_api}/breed/ivalid_breed_name/images"
    r = requests.get(url, timeout=5)

    assert r.status_code == 404
    assert r.json()["status"] == "error"
