from pages.base_page import Page
from pages.checkout_page import CheckoutPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.target_help_page import TargetHelpPage


class Application:

    def __init__(self,driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.signin_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.target_help_page = TargetHelpPage(driver)