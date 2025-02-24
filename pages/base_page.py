from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        self.page.goto(url=url)

    def click(self, locator: str):
        element = self.page.wait_for_selector(selector=locator)
        element.click()

    def input_text(self, locator: str, text: str):
        element = self.page.wait_for_selector(selector=locator)
        element.fill(value=text)

    def get_text(self, locator: str) -> str:
        element = self.page.wait_for_selector(selector=locator)
        return element.inner_text()

    def is_visible(self, locator: str) -> bool:
        is_element = self.page.is_visible(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Элемент не отобразился на странице')

    def is_clickable(self, locator: str) -> bool:
        is_element = self.page.is_enabled(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Элемент не кликабельный')

    def is_not_active_field(self, locator: str) -> bool:
        is_element = self.page.is_disabled(selector=locator)
        if is_element:
            return True
        else:
            raise Exception('Поле активное')

