import pytest
from Pages.ProductsPage import ProductsPage


class Test2:
    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_make_login(self, open_login_page_all_browser):
        login_page = open_login_page_all_browser
        login_page.make_the_login()
        inventory_page = ProductsPage(driver=login_page.driver)
        assert inventory_page.is_url_products(), 'Page not found!'
        assert inventory_page.is_products_title(), 'Product page title is different!'
        assert inventory_page.has_products_in_list(), 'No product images!!'
