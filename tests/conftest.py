import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    page.goto(url='https://www.saucedemo.com/')
    yield page
    page.close()


@pytest.fixture()
def login_page_pl(page):
    return LoginPage(page)

@pytest.fixture()
def product_page(page):
    return ProductPage(page)
