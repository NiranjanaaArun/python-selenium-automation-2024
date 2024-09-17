from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open {UI}")
def open_target(context, UI):
    context.driver.get("https://target.com")
    sleep(2)

@given("{link} Page")
def open_target_circle(context, link):
    context.driver.get("https://www.target.com/circle")
    sleep(7)

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

@then("Verify there are {no_cells} benefit cells")
def verify_benefit_cells(context, no_cells):
    no_of_cells = context.driver.find_elements(By.CSS_SELECTOR, "div[class='cell-item-content']")
    print(no_of_cells)
    assert int(len(no_of_cells)) == 10 , f'{no_of_cells} != 10' # remember , everytime a feature file is read, it is in the form of string, if you have to verify with a integer, convert the string to an integer
    print("testcase passed")