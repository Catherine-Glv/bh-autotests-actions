from locators.main_page_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):

    def login(self, username: str, password: str):
        self.input_text(locator=FIELD_INPUT_LOGIN_LOCATOR, text=username)
        self.input_text(locator=FIELD_INPUT_PASSWORD_LOCATOR, text=password)
        self.click(locator=BUTTON_LOGIN_LOCATOR)

    def get_error_login_message(self):
        return self.get_text(locator=ERROR_MSG_LOGIN_LOCATOR)
