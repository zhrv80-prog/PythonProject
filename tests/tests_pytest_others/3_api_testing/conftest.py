import pytest
import requests

# Добавляем опции url и method

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com",
        help="This is request url"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "delete", "patch"],
        help="method to execute"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))
