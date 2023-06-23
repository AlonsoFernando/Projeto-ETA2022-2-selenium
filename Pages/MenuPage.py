from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class MenuPage(PageObject):

    id_menu_btn = 'react-burger-menu-btn'
    id_close_menu = 'react-burger-cross-btn'
    class_menu_list_items = 'bm-item-list'
    id_logout_item = 'logout_sidebar_link'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu_btn).click()

    def is_menu_open(self):
        try:
            self.driver.find_element(By.ID, self.id_close_menu)
            self.driver.find_element(By.CLASS_NAME, self.class_menu_list_items)
            return True
        except NoSuchElementException:
            return False

    def click_logout(self):
        self.driver.find_element(By.ID, self.id_logout_item).click()

