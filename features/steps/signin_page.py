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

@when("Input incorrect email and password combination")
def incorrect_credentials(context):
    context.app.signin_page.incorrect_credentials()

@when("Click Term and Condition")
def term_and_condition(context):
    context.app.signin_page.term_and_condition()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.signin_page.get_current_window()
    print('Original Window:', context.original_window)

@when('Switch to a terms and conditions window')
def switch_to_new_window(context):
    # sleep(3)
    # all_windows= context.driver.window_handles
    # print('All windows', all_windows)
    # context.driver.switch_to.window(all_windows[1])
    # print('After switch current window:', context.app.target_app_page.get_current_window)
    context.app.signin_page.switch_to_new_window()
    print('After switched', context.app.signin_page.get_current_window())

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

@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions(context):
    context.app.signin_page.verify_tc_opened()
    sleep(3)

@then('User can close new window and switch back to original')
def return_original_window(context):
    context.app.target_app_page.close()
    sleep(3)
    context.driver.switch_to.window(context.original_window)
    # context.app.signin_page.switch_to_window_by_id(context.original_window)
    # sleep(3)

@then('Verify message is shown')
def message_is_shown(context):
    context.app.signin_page.message_is_shown()