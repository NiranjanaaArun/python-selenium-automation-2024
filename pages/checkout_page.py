from pages.base_page import Page
from selenium.webdriver.common.by import By



class CheckoutPage(Page):

    MESSAGE = By.CSS_SELECTOR, "[data-test='boxEmptyMsg']"

    def cart_empty_message(self):
            actual_result = self.driver.find_element(*self.MESSAGE).text
            expected_result = "Your cart is empty"
            assert actual_result == expected_result, f"{actual_result} is not {expected_result}"
