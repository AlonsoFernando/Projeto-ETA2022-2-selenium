from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class CheckoutOverviewPage(PageObject):
    url_overview = 'https://www.saucedemo.com/checkout-step-two.html'
    id_finish_btn = 'finish'
    text_overview = 'Checkout: Overview'
    class_product_name = 'inventory_item_name'

    def __init__(self, driver):
        super(CheckoutOverviewPage, self).__init__(driver=driver)

    def is_overview_page(self):
        return self.is_page(url=self.url_overview, title_text=self.text_overview)

    def click_checkout(self):
        self.driver.find_element(By.ID, self.id_finish_btn).click()

    def view_products(self, name):
        return self.driver.find_element(By.CLASS_NAME, self.class_product_name).text == name
