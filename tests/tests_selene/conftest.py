import pytest
from selene import browser

from tests.tests_qaa_python.test_addoption import base_url


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.window_width = 800
    browser.config.window_height = 600
    browser.config.base_url = 'https://github.com/search'

    yield

    browser.quit()

