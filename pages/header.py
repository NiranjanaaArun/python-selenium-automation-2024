from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Header(Page):
    SEARCH_WORD=(By.ID, 'search')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    CART_ICON = (By.CSS_SELECTOR, "[href*='/icons/Cart.svg#Cart']")


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_WORD)
        self.click(*self.SUBMIT_BUTTON)
        sleep(6)


    def cart_icon(self):
        self.click(*self.CART_ICON)
        sleep(6)