import pytest
from playwright.sync_api import sync_playwright


def test_my():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.route()

        # Открываем сайт
        page.goto("https://github.com/")

        # Ждем пока страница загрузится
        page.wait_for_load_state("networkidle")

        # Пауза
        page.wait_for_timeout(1000)

        # Проверка
        assert page.locator("text=The future of building happens together").is_visible(), "Error"

        # Закрываем браузер
        browser.close()


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
# def test_check_empty_cart_with_mock():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#
#         context = browser.new_context()
#         page = context.new_page()
#
#         # 1 Настраиваем перехват (до загрузки страницы)
#         def hendle_route(route):
#             # Здесь мы говорим "Если запрос идет на /api/cart"
#             if route.request.url.endswith("/_graphql?body=%7B%22persistedQueryName%22%3A%22OpenClosedTabsQuery%22%2C%22query%22%3A%229b5335baab0566640cfa28c329582507%22%2C%22variables%22%3A%7B%22name%22%3A%22Evaluation_AI_course%22%2C%22owner%22%3A%22meshkovQA%22%2C%22query%22%3A%22is%3Aissue%20archived%3Afalse%20repo%3AmeshkovQA%2FEvaluation_AI_course%20sort%3Acreated-desc%22%2C%22type%22%3A%22ISSUE_HYBRID%22%7D%7D"):
#                 # ... то мы не идём на сервер, а отдаём свой JSON (пустую корзину)
#                 route.fulfill(
#                     status=200,
#                     content_type="application/json",
#                     body='{"items": [], "total": 0}' # Подмена ответа
#                 )
#             else:
#                 # Если запрос не про нас - пропускаем как есть
#                 route.continue_()
#
#         # 2 Включаем перехват всех запросов на странице
#         page.route("**/*", hendle_route) # **/* означает ловить все запросы
#
#         # 3 Открываем страницу (Теперь playwright сам подставит наш фейковый ответ)
#         page.goto("https://github.com/_graphql?body=%7B%22persistedQueryName%22%3A%22OpenClosedTabsQuery%22%2C%22query%22%3A%229b5335baab0566640cfa28c329582507%22%2C%22variables%22%3A%7B%22name%22%3A%22Evaluation_AI_course%22%2C%22owner%22%3A%22meshkovQA%22%2C%22query%22%3A%22is%3Aissue%20archived%3Afalse%20repo%3AmeshkovQA%2FEvaluation_AI_course%20sort%3Acreated-desc%22%2C%22type%22%3A%22ISSUE_HYBRID%22%7D%7D")
#
#         # 4 Проверяем что настранице появилась надпись "No results"
#         assert page.locator("text=Try adjusting your search filters.").is_visible()
#
#         browser.close()


def test_mock_response_500():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        # 1 Настраиваем перехват (до загрузки страницы)
        def hendle_route(route):
            # Здесь мы говорим "Если запрос идет на /api/cart"
            if route.request.url.endswith("/api/cart"):
                # ... то мы не идём на сервер, а отдаём свой JSON (пустую корзину)
                route.fulfill(
                    status=500,
                    content_type="application/json",
                    body='{"error": "Internal Server Error"}'
                )
            else:
                # Если запрос не про нас - пропускаем как есть
                route.continue_()

        # 2 Включаем перехват всех запросов на странице
        page.route("**/*", hendle_route) # **/* означает ловить все запросы

        # 3 Открываем страницу (Теперь playwright сам подставит наш фейковый ответ)
        page.goto("https://тестовый магазин.ru/cart")

        # 4 Проверяем что настранице появилась надпись "Корзина пуста"
        assert page.locator("text=корзина пуста").is_visible()

        browser.close()
