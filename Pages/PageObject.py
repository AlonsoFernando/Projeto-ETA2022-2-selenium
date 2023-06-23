from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:
    class_title = 'title'

    def __init__(self, driver=None, browser='Chrome'):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                raise Exception('Browser não suportado!')
            self.driver.implicitly_wait(3)

    def is_url(self, url):
        return self.driver.current_url == url

    def is_title(self, text_title):
        return self.driver.find_element(By.CLASS_NAME, self.class_title).text == text_title

    def is_page(self, url, title_text):
        return self.is_url(url) and self.is_title(title_text)

    def save_screenshot_page(self):
        self.driver.save_screenshot('screenshot_page.png')

    def close(self):
        self.driver.quit()
