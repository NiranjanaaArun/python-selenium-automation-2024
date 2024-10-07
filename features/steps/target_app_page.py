from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open Target App Page2')
def open_app_page(context):
        context.app.target_app_page.open_target_app()

@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()
    print('Original Window:', context.original_window)

@when('Click Privacy Policy Link')
def click_privacy_policy(context):
    context.app.target_app_page.click_privacypolicy_link()

@when('Switch to a new window')
def switch_to_new_window(context):
    # sleep(3)
    # all_windows= context.driver.window_handles
    # print('All windows', all_windows)
    # context.driver.switch_to.window(all_windows[1])
    # print('After switch current window:', context.app.target_app_page.get_current_window)
    context.app.target_app_page.switch_to_new_window()
    print('After switched', context.app.target_app_page.get_current_window())

@then('Verify privacy policy page opened')
def verify_privacy_policy(context):
    context.app.target_app_page.verify_page_opened()
    sleep(3)

@then('Close the current page')
def close_page(context):
    context.app.target_app_page.close()
    sleep(3)
    print('The window is closed')

@then('Return to the original window')
def return_original_window(context):
    # context.driver.switch_to.window(context.original_window)
    context.app.target_app_page.switch_to_window_by_id(context.original_window)
    sleep(3)