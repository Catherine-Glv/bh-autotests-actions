import pytest
from playwright.sync_api import sync_playwright
from pages.product_page import ProductPage

class TestProductPage:

    def test_product_count(self, login_page_pl, product_page):
        login_page_pl.login(username='standard_user', password='secret_sauce')
        get_product_items = product_page.get_product_count()
        expected_products_count = 6
        assert get_product_items == expected_products_count, (f"Ожидалось {expected_products_count} товаров в каталоге, "
                                                              f"фактически на странице {get_product_items}")

    def test_menu_burger(self, login_page_pl, product_page):
        login_page_pl.login(username='standard_user', password='secret_sauce')
        assert product_page.all_items_is_visible(), "Меню All Items не отобразилось"
        assert product_page.about_is_visible(), "Меню About не отобразилось"
        assert product_page.logout_is_visible(), "Меню Logout не отобразилось"
        assert product_page.reset_items_is_visible(), "Меню Reset app state не отобразилось"

