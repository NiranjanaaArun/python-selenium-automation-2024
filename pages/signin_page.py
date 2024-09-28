from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignInPage(Page):

    SIGNIN_TEXT = (By.CSS_SELECTOR, "[class*='border-radius'] h1")
    EMAIL = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SIGNIN_BUTTON = (By.ID, 'login')

    def verify_page_opened(self):

        expected_result = "Sign into your Target account"
        #self.verify_text(expected_result, *self.SIGNIN_TEXT)
        actual_result = self.driver.find_element(*self.SIGNIN_TEXT).text
        expected_result = "Sign into your Target account"
        assert actual_result == expected_result, \
            f'actual_result: {actual_result} not equal to expected_result: {expected_result}'


    def input_email_password(self):
        self.input_text('mrbad101@cakdays.com', *self.EMAIL)
        sleep(4)
        self.input_text('****', *self.PASSWORD)
        sleep(4)
        self.click(*self.SIGNIN_BUTTON)
        sleep(5)
