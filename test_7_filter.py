import pytest
from Pages.ProductsPage import ProductsPage


class Test7:
    @pytest.fixture(autouse=True)
    def setup(self, login_saucedemo):
        self.login_saucedemo = login_saucedemo

    def test_default_sort_order(self):
        product_page = ProductsPage(driver=self.login_saucedemo.driver)
        product_names = product_page.get_product_names()
        sorted_names = sorted(product_names)
        assert product_names == sorted_names, "Products are not sorted alphabetically"

    def test_reverse_sort_order(self):
        product_page = ProductsPage(driver=self.login_saucedemo.driver)
        product_page.select_sort_option("Name (Z to A)")
        product_names = product_page.get_product_names()
        sorted_names = sorted(product_names, reverse=True)
        assert product_names == sorted_names, "Products are not sorted in reverse alphabetical order"

    def test_sort_by_price_low_to_high(self):
        product_page = ProductsPage(driver=self.login_saucedemo.driver)
        product_page.select_sort_option("Price (low to high)")
        product_names = product_page.get_product_names()
        sorted_names = sorted(product_names, key=lambda x: int(x[x.index("$")+1:]) if "$" in x else 0)
        assert product_names == sorted_names, "Products are not sorted by price from low to high"

    def test_sort_by_price_high_to_low(self):
        product_page = ProductsPage(driver=self.login_saucedemo.driver)
        product_page.select_sort_option("Price (high to low)")
        product_names = product_page.get_product_names()
        sorted_names = sorted(product_names, key=lambda x: int(x[x.index("$")+1:]) if "$" in x else 0, reverse=True)
        assert product_names == sorted_names, "Products are not sorted by price from high to low"
