from locators.product_page_locators import *
from pages.base_page import BasePage

class ProductPage(BasePage):

    def get_product_items(self):
        return self.page.locator(PRODUCT_ITEMS)

    def get_product_count(self):
        return self.get_product_items().count()

    def all_items_is_visible(self):
        self.click(BURGER_MENU)
        return self.page.locator(BURGER_MENU_ALL_ITEMS)

    def about_is_visible(self):
        return self.page.locator(BURGER_MENU_ABOUT)

    def logout_is_visible(self):
        return self.page.locator(BURGER_MENU_LOGOUT)

    def reset_is_visible(self):
        return self.page.locator(BURGER_MENU_RESET)
