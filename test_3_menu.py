from Pages.MenuPage import MenuPage


class Test3:
    def test_logout(self, login_saucedemo):
        menu_page = MenuPage(driver=login_saucedemo.driver)
        menu_page.open_menu()
        assert menu_page.is_menu_open(), 'Menu has not been opened'
        menu_page.click_logout()
        assert login_saucedemo.is_url_login(), 'Login page not found'
