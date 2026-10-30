import os
import pytest
import requests
from allure_commons._allure import step
from selene import browser, be, have

@pytest.fixture(scope="session")
def login_though_api():
    password = os.getenv("MY_APP_PASSWORD")
    email = 'Ivanov@123.com'

    data = {
        'Email': email,
        'Password': password,
        'RememberMe': False}

    requests.post('https://demowebshop.tricentis.com/login', data=data) #allow_redirects=False

    yield

    requests.get('https://demowebshop.tricentis.com/logout')

@pytest.fixture(scope="session")
def login_though_ui():
    url = 'https://demowebshop.tricentis.com/login'

    email = 'Ivanov@123.com'
    password = os.getenv("MY_APP_PASSWORD")

    browser.open(url)
    browser.element('#Email').send_keys(email)
    browser.element('#Password').send_keys(password)
    browser.element('[class="button-1 login-button"]').click()

    try:
        yield
    finally:
        # Этот блок выполнится ВСЕГДА, даже если тест упал
        try:
            browser.element('[class="ico-logout"]').click()
            browser.element('.ico-logout').should(be.hidden)
        except Exception:
            pass
        browser.quit()






