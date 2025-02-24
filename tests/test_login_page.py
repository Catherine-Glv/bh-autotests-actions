import allure


@allure.feature('login_page')
class TestLoginPage:

    @allure.story('Тест hp авторизации')
    def test_hp_login(self, login_page_pl):
        login_page_pl.login(username='standard_user', password='secret_sauce')
        assert login_page_pl.is_visible(locator="//div[@class='header_secondary_container']")

    @allure.story('Тест получения ошибки авторизации')
    def test_error_message(self, login_page_pl):
        login_page_pl.login(username='standard_user', password='1234')
        assert login_page_pl.is_visible(locator="//div[@class='header_secondary_container']")
