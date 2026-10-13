import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "delete", "patch"],
        help="method to execute"
    )

# Фикстура для url
@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

# Фикстура для method
@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))

