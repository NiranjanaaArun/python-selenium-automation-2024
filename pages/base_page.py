from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self,url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        return self.driver.find_element(*locator).text

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_to_be_clickable(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        )

    def wait_to_be_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        ).click()

    def wait_until_appears(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(*locator),
            message=f'Element by {locator} does not appear')

    def wait_until_disappears(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(*locator),
            message=f'Element by {locator} still shown'
        )

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text==actual_text, f'{expected_text} != {actual_text}'

    def partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert  expected_text in actual_text, f'{expected_text} not in {actual_text}'

    def verify_url(self, expected_url):
        current_url = self.driver.current_url
        assert expected_url == current_url, f'{expected_url} != {current_url}'

    def partial_url(self, expected_url):
        current_url = self.driver.current_url
        assert expected_url in current_url, f'{expected_url} not in {current_url}'

