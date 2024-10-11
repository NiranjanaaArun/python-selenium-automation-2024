from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self,url):
        logger.info(f'open url: {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f'finding an element: {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'finding all elements: {locator}')
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        logger.info(f'get the text: {locator}')
        return self.driver.find_element(*locator).text

    def click(self, *locator):
        logger.info(f'clicking on element: {locator}')
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
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} does not appear')

    def wait_until_disappears(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} still shown'
        )

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All windows', all_windows)
        print(f'Switching to window, {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print(f'Switching to window, {window_id}')
        self.driver.switch_to.window(window_id)

    def close(self):
        self.driver.close()

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

