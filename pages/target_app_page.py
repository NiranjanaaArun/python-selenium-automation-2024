from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class TargetAppPage(Page):
    PP_link = (By.XPATH, "//a[text()='Privacy policy']")

    def open_target_app(self):
        self.open('https://www.target.com/c/target-app/')

    def click_privacypolicy_link(self):
        self.wait_to_be_clickable_click(*self.PP_link)

    def verify_page_opened(self):
        self.partial_url('terms-conditions/')




