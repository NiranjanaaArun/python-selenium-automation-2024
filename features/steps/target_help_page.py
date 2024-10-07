from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given("Open TargetHelp")
def target_help_page(context):
    context.app.target_help_page.open_help_page()

@when("Click on search")
def click_on_search(context):
    context.app.target_help_page.click_search()

@when("Choose dropdown")
def click_on_dropdown(context):
    context.app.target_help_page.click_dropdown()

@then("Verify correct page is opened")
def verify_correct_page(context):
    context.app.target_help_page.verify_correct_page()