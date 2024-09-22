from pages.base_page import Page
from pages.checkout_page import CheckoutPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self,driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.checkout_page = CheckoutPage(driver)