import pytest
import requests


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def expected_status_code(request):
    return request.config.getoption("--status_code")


def test_add_option_success(base_url, expected_status_code):
    """Проверяет, что URL возвращает ожидаемый статус-код."""
    res = requests.get(base_url, timeout=5)

    assert res.status_code == expected_status_code, (
        f"URL: {base_url}, "
        f"ожидался {expected_status_code}, получен {res.status_code}"
    )