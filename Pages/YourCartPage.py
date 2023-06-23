from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class YourCartPage(PageObject):
    url_cart = 'https://www.saucedemo.com/cart.html'
    text_your_cart = 'Your Cart'
    id_checkout = 'checkout'
    class_product_name = 'inventory_item_name'

    def __init__(self, driver):
        super(YourCartPage, self).__init__(driver=driver)

    def is_your_cart_page(self):
        return self.is_page(url=self.url_cart, title_text=self.text_your_cart)

    def click_checkout(self):
        self.driver.find_element(By.ID, self.id_checkout).click()

    def has_product_in_cart(self, name):
        return self.driver.find_element(By.CLASS_NAME, self.class_product_name).text == name
