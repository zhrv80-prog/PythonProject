import pytest
from playwright.sync_api import sync_playwright


def test_mock_simple_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        def handle_route(route):
            url = route.request.url
            print(f" Запрос: {url}")

            # Перехватываем ЛЮБОЙ запрос к GitHub
            if "github.com" in url:
                print(f"Перехвачен запрос: {url}")

                # Подменяем ВСЕ на нашу страницу
                route.fulfill(

                    # status=500,
                    # content_type="application/json",
                    # body='{"error": "Internal Server Error"}'

                    status=200,
                    content_type="text/html",
                    body="""
                    <html>
                        <head><title>Replace</title></head>
                        <body>
                            <h1 id="main-title">Traffic catch works!</h1>
                            <p>This page was replaced with Playwright</p>
                            <div id="test">No results</div>
                        </body>
                    </html>
                    """
                )
            else:
                # Запросы не к GitHub пропускаем
                route.continue_()

        # Включаем перехват ДО загрузки страницы
        page.route("**/*", handle_route)

        # Открываем GitHub
        page.goto("https://github.com")

        # Ждем, пока страница загрузится
        page.wait_for_load_state("networkidle")

        # Делаем небольшую паузу
        page.wait_for_timeout(1000)

        # Проверяем через ID (надежнее)
        assert page.locator("#main-title").is_visible()
        print("Тест прошел!")

        browser.close()