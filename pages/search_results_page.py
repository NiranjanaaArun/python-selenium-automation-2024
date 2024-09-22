from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep

class SearchResultsPage(Page):

    SEARCH_RESULTS_HEADER = (By.CSS_SELECTOR, "div[data-test='results-facets-row'] span[class*='display']")
    def verify_results_header(self,product):

        actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text

        assert product in actual_result, f'Expected {product} but got {actual_result}'