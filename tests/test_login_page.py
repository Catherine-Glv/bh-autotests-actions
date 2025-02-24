class TestLoginPage:

    def test_hp_login(self, login_page_pl):
        login_page_pl.login(username='standard_user', password='secret_sauce')
        assert login_page_pl.is_visible(locator="//div[@class='header_secondary_container']")
