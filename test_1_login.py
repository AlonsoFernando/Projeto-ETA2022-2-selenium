
class Test1:
    def test_click_login_btn(self, setup):
        login_page = setup
        login_page.click_login_btn()
        assert login_page.is_url_login(), 'Error Page'
        assert login_page.has_login_message_error(), "Wrong message!"
