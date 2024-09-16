from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open target.com")
def open_target(context):
    context.driver.get("https://target.com")
    sleep(2)

@when("Click Sign In")
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "span[class*='sc-58ad44c0-3 kwbrXj']").click()
    context.driver.find_element(By.CSS_SELECTOR, "[href='/account']").click()
    sleep (4)

@then("Verify Sign In form opened")
def verify_sign_in(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='e064f5c-0 sc-315b8ab9-']").text
    expected_result = "Sign into your Target account"
    assert actual_result == expected_result, f'{actual_result} != {expected_result}'
    print("testcase passed")
