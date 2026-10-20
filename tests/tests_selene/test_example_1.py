import pytest
from selene import browser, be, have


# github успешный поиск
def test_github_success_search():
    browser.open('https://github.com/search')
    browser.element('[aria-label="Search GitHub"]').type('qa.guru').press_enter()
    browser.element('[data-testid="results-list"]').should(have.text('QA.GURU'))
    browser.close()


# github неуспешный поиск
def test_github_failures_search():
    browser.open('https://github.com/search')
    browser.element('[aria-label="Search GitHub"]').type('qa.guru').press_enter()
    browser.element('[data-testid="results-list"]').should(have.text('Failure'))
    browser.close()


# duckduckgo успешный поиск
def test_duckduckgo_success_search():
    browser.open('https://duckduckgo.com')
    browser.element(
        '[class="search-toggle-box-module-scss-module__ul1rLa__queryInput inline-ai-search-box-module-scss-module__eJ3y5G__queryInput"]').type(
        'lenta').press_enter()
    browser.element('[class="qrc3T8W2PIYg9L63oA06 IlK3G8WDnnjkNGDV6qzo h3EKGeHmRRkjbMqYfNUi wuwdN2SgDOTwsnBO5PI7 rXBzGoYc_uM83jRoODrM xWVFEW_kM7bYLASLNfsZ"]').should(have.text('Lenta'))
    browser.close()


# duckduckgo неуспешный поиск
def test_duckduckgo_failures_search():
    browser.open('https://duckduckgo.com')
    browser.element(
        '[class="search-toggle-box-module-scss-module__ul1rLa__queryInput inline-ai-search-box-module-scss-module__eJ3y5G__queryInput"]').type(
        'lenta').press_enter()
    browser.element('[class="qrc3T8W2PIYg9L63oA06 IlK3G8WDnnjkNGDV6qzo h3EKGeHmRRkjbMqYfNUi wuwdN2SgDOTwsnBO5PI7 rXBzGoYc_uM83jRoODrM xWVFEW_kM7bYLASLNfsZ"]').should(have.text('rhgsheshserseh'))
    browser.close()


# ya успешный поиск
def test_ya_success_search():
    browser.open('https://ya.ru ')
    browser.element(
        '[class="search3__input mini-suggest__input"]').type(
        'lenta').press_enter()
    browser.element(
        '[class="b-page__body i-ua Typo Typo_text_m Typo_line_m b-page b-page_tld_ru b-page_ajax_yes b-page_initial-scroll_yes b-page_white-bg_yes pointerfocus beauty-scroll-big Theme_root_serp-desktop i-ua_platform_other i-ua_js_inited"]').should(
        have.text('Lenta'))

    browser.close()


# ya неуспешный поиск
def test_ya_success_search():
    browser.open('https://ya.ru ')
    browser.element(
        '[class="search3__input mini-suggest__input"]').type(
        'lenta').press_enter()
    browser.element(
        '[class="b-page__body i-ua Typo Typo_text_m Typo_line_m b-page b-page_tld_ru b-page_ajax_yes b-page_initial-scroll_yes b-page_white-bg_yes pointerfocus beauty-scroll-big Theme_root_serp-desktop i-ua_platform_other i-ua_js_inited"]').should(
        have.text('kjsdghlhgjl'))

    browser.close()
