from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SearchResultsPage(Page):

    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, "div[data-test='results-facets-row'] span[class*='display']")
    ITEM1 = (By.CSS_SELECTOR, 'div[data-focusid*="_product_card"] button[data-test="chooseOptionsButton"]')
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    CHECKOUT = (By.CSS_SELECTOR, "[href='/cart']")

    def verify_results_header(self,product):
        actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert product in actual_result, f'Expected {product} but got {actual_result}'

    def add_item_to_cart(self):
        sleep(3)
        self.click(*self.ITEM1)
        sleep(4)
        self.click(*self.SIDE_NAV_ADD_TO_CART_BTN)
        sleep(4)
        self.click(*self.CHECKOUT)


