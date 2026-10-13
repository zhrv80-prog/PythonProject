import pytest
import requests


@pytest.fixture(scope="session")
def dog_url_api():
    """Базовый url api"""
    return "https://dog.ceo/api"


@pytest.fixture(scope="session")
def openbrewerydb_url_api():
    """Базовый url api"""
    return "https://api.openbrewerydb.org/"

@pytest.fixture(scope="session")
def jsonplaceholder_url_api():
    """Базовый url api """
    return "https://jsonplaceholder.typicode.com/"

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",
        action="store",
        default=1
    )
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help = "url api"
    )
    parser.addoption(
       "--status_code",
        action="store",
        default=200,
        type = int,
        help = "status_code"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")