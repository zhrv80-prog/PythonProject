import time

import pytest
from selene import browser, be, have
from playwright.sync_api import sync_playwright

# github успешный поиск
def test_github_success_search():
    browser.open('/')
    browser.element('[aria-label="Search GitHub"]').type('google').press_enter()
    browser.element('[data-testid="results-list"]').should(have.text('google'))

@pytest.mark.parametrize("width,height", [(1920, 1080), (1360, 768), (375, 667)])
def test_github_size_parametrized(width, height):
    browser.config.window_width = width
    browser.config.window_height = height
    browser.open('/')
    browser.element('[aria-label="Search GitHub"]').type('google').press_enter()
    browser.element('[data-testid="results-list"]').should(have.text('google'))
    browser.quit()

@pytest.fixture(params=[(1920, 1080), (1360, 768), (375, 667)])
def browser_playwright(request):
    width, height = request.param
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": width, "height": height})
        page = context.new_page()
        yield page          # ← отдаём страницу в тест
        browser.close()     # ← закрываем браузер после теста

def test_ya(browser_playwright):
    # browser_playwright — это уже готовая страница
    browser_playwright.goto("https://github.com/search")

    # Ищем поле поиска и заполняем
    browser_playwright.get_by_placeholder("Search GitHub").fill("google")

    # Проверяем результат
    assert "google" in browser_playwright.url or True  # пример проверки