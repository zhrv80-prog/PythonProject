from playwright.sync_api import sync_playwright

# ===== Пример теста на playwright ====
def test_open_page(config): # config from conftest.py
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page() # new page
        page.goto(config["base_url"])
        browser.close()