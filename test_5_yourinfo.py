from Pages.CheckoutCompletePage import CheckoutCompletePage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.CheckoutYourInformationPage import CheckoutYourInformationPage
from Pages.ProductsPage import ProductsPage
from Pages.YourCartPage import YourCartPage


class Test5:
    def test_checkout_success(self, login_saucedemo):
        products_page = ProductsPage(driver=login_saucedemo.driver)
        product_name = products_page.add_random_product_to_cart()
        products_page.open_cart_page()
        your_cart_page = YourCartPage(driver=products_page.driver)
        your_cart_page.click_checkout()
        checkout_your_info = CheckoutYourInformationPage(driver=your_cart_page.driver)
        assert checkout_your_info.is_checkout_your_information_page(), 'Checkout: Your information page not found'
        checkout_your_info.fill_in_the_fields()
        checkout_overview = CheckoutOverviewPage(driver=checkout_your_info.driver)
        assert checkout_overview.is_overview_page(), 'Overview page not found'
        assert checkout_overview.view_products(name=product_name), 'Product not found'
        checkout_overview.click_checkout()
        checkout_complete = CheckoutCompletePage(driver=checkout_overview.driver)
        assert checkout_complete.is_complete_page(), 'Checkout: Complete page not found'
        assert checkout_complete.view_thank(), 'Message not found'
