import pytest
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='Browser to run the tests.')


@pytest.fixture()
def open_login_page_all_browser(all_browser):
    login_page = LoginPage(browser=all_browser)
    yield login_page
    login_page.save_screenshot_page()
    login_page.close()


@pytest.fixture()
def setup(request):
    select_browser = request.config.getoption('--browser').lower()
    login_page = LoginPage(browser=select_browser)
    yield login_page
    login_page.save_screenshot_page()
    login_page.close()


@pytest.fixture()
def login_saucedemo(setup):
    login_page = setup
    login_page.make_the_login()
    yield login_page


@pytest.fixture()
def one_product_in_cart(login_saucedemo):
    product_page = ProductsPage(driver=login_saucedemo.driver)
    product_page.add_random_product_to_cart()
    yield product_page
