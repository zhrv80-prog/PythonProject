import os
from pprint import pprint
from time import sleep

import requests
import pytest
from allure_commons._allure import step
from selene import browser, have


def test_add_to_cart():
    web_url = "https://demowebshop.tricentis.com/"
    api_url = 'https://demowebshop.tricentis.com/login'
    password = os.getenv("MY_APP_PASSWORD")
    email = 'Ivanov@123.com'

    data = {
        'Email': email,
        'Password': password,
        'RememberMe': False}

    result = requests.post(url=api_url, data=data, allow_redirects=False)
    cookies = result.cookies.get("NOPCOMMERCE.AUTH")
    browser.open(web_url)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    browser.open(web_url)

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(email))
    sleep(5)

    url_add_to_cart = 'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1'
    response_add_to_cart = requests.post(url_add_to_cart)

    browser.open(url_add_to_cart)
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    browser.open('https://demowebshop.tricentis.com/cart').should

    with step("Verify successful addition to cart"):
        browser.element('[name="updatecart"]').should(have.value("Update shopping cart"))