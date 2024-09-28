from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target")
def open_target(context):
    # context.driver.get("https://target.com")
    # sleep(2)
    context.app.main_page.open_main()
    sleep(4)

@given("{link} Page")
def open_target_circle(context, link):
    context.driver.get("https://www.target.com/circle")
    sleep(7)

@when("Click Sign In")
def sign_in(context):
    # context.driver.find_element(By.CSS_SELECTOR, "span[class*='sc-58ad44c0-3 kwbrXj']").click()
    # context.driver.find_element(By.CSS_SELECTOR, "[href='/account']").click()
    # sleep (4)
    context.app.header.sign_in_button()
    sleep(4)

@when("Input email and password on SignIn page")
def email_password (context):
    context.app.signin_page.input_email_password()

@then("Verify Sign In form opened")
def verify_sign_in(context):
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='e064f5c-0 sc-315b8ab9-']").text
    # expected_result = "Sign into your Target account"
    # assert actual_result == expected_result, f'{actual_result} != {expected_result}'
    # print("testcase passed")
    context.app.signin_page.verify_page_opened()

@then("Verify there are {no_cells} benefit cells")
def verify_benefit_cells(context, no_cells):
    no_of_cells = context.driver.find_elements(By.CSS_SELECTOR, "div[class='cell-item-content']")
    print(no_of_cells)
    assert int(len(no_of_cells)) == 10 , f'{no_of_cells} != 10' # remember , everytime a feature file is read, it is in the form of string, if you have to verify with a integer, convert the string to an integer
    print("testcase passed")

@then("Verify user is logged in")
def verify_user(context):
    context.app.main_page.sign_in_disappear()