import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) # браузер не показывается
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.example.com/")
    page.get_by_role("link", name="Learn more").click()
    page.get_by_role("link", name="IANA-managed Reserved Domains").click()
    page.get_by_role("link", name="Special-Use Domain Names").first.click()
    page.get_by_role("link", name="Special-Use Domain Names").click()
    page.locator("tr:nth-child(15) > td:nth-child(2) > a").click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name=" html").click()
    page1 = page1_info.value
    page1.close()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
