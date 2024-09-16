from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open Target page')
def target_page(context):
    context.driver.get('https://www.target.com')

@when('Click cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='/icons/Cart.svg#Cart']").click()

@then('“Your cart is empty” message is shown')
def message_is_shown(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")
    expected_result = "Your cart is empty"

    assert actual_result.text == expected_result, f'Expected {expected_result} but got {actual_result.text}'
    print("Test Case passed")
