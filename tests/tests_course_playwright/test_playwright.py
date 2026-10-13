from playwright.sync_api import sync_playwright

def test_open_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.example.com")
        print(f"\n123 {page.title()}")
        browser.close()

def test_open_page1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.example.com")
        assert page.title() == "Example Domain"
        browser.close()


if __name__ == "__main__":
   test_open_page()