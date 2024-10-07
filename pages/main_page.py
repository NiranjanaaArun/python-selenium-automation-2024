from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):

    ELEMENT = (By.CSS_SELECTOR, 'div div h1')

    def open_main(self):
        self.open('https://www.target.com')

    def sign_in_disappear(self):
        sleep(4)
        self.verify_text('Introducing passkeys', *self.ELEMENT)


