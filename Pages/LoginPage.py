from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class LoginPage(PageObject):
    url_login = 'https://www.saucedemo.com/'
    id_login_btn = 'login-button'
    class_error_msg = 'error-message-container'
    txt_error_message = 'Epic sadface: Username is required'
    id_username = 'user-name'
    id_password = 'password'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.get(self.url_login)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def is_url_login(self):
        return self.is_url(url=self.url_login)

    def has_login_message_error(self):
        error_message = self.driver.find_element(By.CLASS_NAME, self.class_error_msg).text
        return error_message == self.txt_error_message

    def make_the_login(self, username='standard_user', password='secret_sauce'):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)
        self.driver.find_element(By.ID, self.id_password).send_keys(password)
        self.click_login_btn()
