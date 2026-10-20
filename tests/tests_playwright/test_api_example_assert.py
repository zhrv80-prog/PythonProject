from playwright.sync_api import expect


def test_post_request(api_request_context, config):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = api_request_context.post(
        f"{config['api_base_url']}posts", data=payload
    )
    expect(response).to_be_ok()
    data = response.json()
    assert data["title"] == "foo", "Поле 'title' не совпадает"
    assert data["body"] == "bar", "Поле 'body' не совпадает"
    assert data["userId"] == 1, "Поле 'userId' не совпадает"
    assert "id" in data, "Поле 'id' отсутствует"
