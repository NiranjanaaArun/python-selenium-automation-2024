from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TargetHelpPage(Page):

    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[type='image'][name*='id']")
    DD= (By.CSS_SELECTOR, "select[id*='viewHelpTopics']")

    def open_help_page(self):
        self.open("https://help.target.com/help")

    def click_search(self):
        self.click(*self.SEARCH_BUTTON)

    def click_dropdown(self):
        dropdown_menu = self.find_element(*self.DD)
        select = Select(dropdown_menu)
        select.select_by_value('Payment Options')

    def verify_correct_page(self):
        self.partial_url('Payment+Options&')







