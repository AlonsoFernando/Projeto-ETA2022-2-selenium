from random import randint
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject
from selenium.webdriver.support.ui import Select


class ProductsPage(PageObject):
    url_products = 'https://www.saucedemo.com/inventory.html'
    class_title = 'title'
    txt_products_title = 'Products'
    class_products_list = 'inventory_list'
    class_product_card = 'inventory_item'
    class_add_to_cart_btn = 'btn_primary'
    class_shopping_cart_badge = 'shopping_cart_badge'
    class_shopping_cart_icon = 'shopping_cart_link'
    class_remove_btn = 'btn_secondary'
    text_remove_btn = 'Remove'
    class_product_item_name = 'inventory_item_name'
    class_products_sorted = "product_sort_container"

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)
        self.driver = driver

    def is_url_products(self):
        return self.is_url(url=self.url_products)

    def is_products_title(self):
        return self.is_title(self.txt_products_title)

    def has_products_in_list(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.class_products_list)
            return True
        except NoSuchElementException:
            return False

    def add_random_product_to_cart(self):
        products_card_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_card)
        random_product_index = randint(0, len(products_card_list) - 1)
        product_card = products_card_list[random_product_index]
        product_card.find_element(By.CLASS_NAME, self.class_add_to_cart_btn).click()
        btn_text = product_card.find_element(By.CLASS_NAME, self.class_remove_btn).text
        if btn_text != self.text_remove_btn:
            raise Exception('The button does not contain the text REMOVE')
        if self.get_card_number() != '1':
            raise Exception('Product not adding to shopping cart')
        return product_card.find_element(By.CLASS_NAME, self.class_product_item_name).text

    def get_card_number(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_badge).text

    def open_cart_page(self):
        self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_icon).click()

    def select_sort_option(self, option_text):
        sort_dropdown = Select(self.driver.find_element(By.CLASS_NAME, self.class_products_sorted))
        sort_dropdown.select_by_visible_text(option_text)

    def get_product_names(self):
        product_elements = self.driver.find_elements(By.CLASS_NAME, self.class_product_item_name)
        product_names = [element.text for element in product_elements]
        return product_names
