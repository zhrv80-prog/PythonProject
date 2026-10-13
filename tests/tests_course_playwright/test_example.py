from playwright.sync_api import sync_playwright

def test_open_page(config):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(config["base_url"])
        browser.close()