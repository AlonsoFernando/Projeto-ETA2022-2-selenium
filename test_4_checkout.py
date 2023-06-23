from Pages.CheckoutYourInformationPage import CheckoutYourInformationPage
from Pages.YourCartPage import YourCartPage


class Test4:
    def test_error_message_checkout_information(self, one_product_in_cart):
        one_product_in_cart.open_cart_page()
        your_cart_page = YourCartPage(driver=one_product_in_cart.driver)
        assert your_cart_page.is_your_cart_page(), 'Your cart page not found'
        your_cart_page.click_checkout()

        checkout_your_info = CheckoutYourInformationPage(driver=your_cart_page.driver)
        assert checkout_your_info.is_checkout_your_information_page(), 'Checkout: Your information page not found'
        checkout_your_info.click_continue()
        assert checkout_your_info.is_checkout_your_information_page(), 'Checkout: Your information page not found'
        assert checkout_your_info.has_first_name_error_message(), 'Error message not found'

