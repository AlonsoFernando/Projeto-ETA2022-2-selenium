from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class CheckoutCompletePage(PageObject):
    url_overview = 'https://www.saucedemo.com/checkout-complete.html'
    id_back_home_btn = 'back-to-products'
    text_complete = 'Checkout: Complete!'
    text_thanks = 'Thank you for your order!'
    class_complete = 'complete-header'

    def __init__(self, driver):
        super(CheckoutCompletePage, self).__init__(driver=driver)

    def is_complete_page(self):
        return self.is_page(url=self.url_overview, title_text=self.text_complete)

    def click_back_home(self):
        self.driver.find_element(By.ID, self.id_back_home_btn).click()

    def view_thank(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_complete).text
