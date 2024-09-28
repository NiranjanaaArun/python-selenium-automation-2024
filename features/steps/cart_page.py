from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

item1 = (By.CSS_SELECTOR, 'div[data-focusid*="_product_card"] button[data-test="chooseOptionsButton"]')
side_nav_add_to_cart_btn = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
item2= (By.CSS_SELECTOR, "[href*='iced-tea-drink-52-fl-oz/-/A-13186053#lnk=sametab']")
item3= (By.CSS_SELECTOR, "[href*='stress-16ct/-/A-81503691#lnk=sametab']")
continue_shopping = (By.CSS_SELECTOR, '[data-test="content-wrapper"] div[class*="styles_topOnlySmallScreen"] button')
checkout = (By.CSS_SELECTOR, "[href='/cart']")
cart = (By.CSS_SELECTOR, "div.h-margin-l-x2 span")

@given('Open Target page')
def target_page(context):
#     context.driver.get('https://www.target.com')
    context.app.main_page.open_main()


@when('Click cart icon')
def click_cart_icon(context):
    # context.driver.find_element(By.CSS_SELECTOR, "[href*='/icons/Cart.svg#Cart']").click()
    context.app.header.cart_icon()


@when('Add items into cart')
def added_items(context):
    context.driver.execute_script("window.scrollBy(0, 700)")
    sleep(2)
    # context.driver.find_element(*item1).click()
    # sleep(3)
    # context.driver.find_element(*side_nav_add_to_cart_btn).click()
    # sleep(4)
    # context.driver.find_element(*checkout).click()
    context.app.search_results_page.add_item_to_cart()


@then('“Your cart is empty” message is shown')
def message_is_shown(context):
    # actual_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")
    # expected_result = "Your cart is empty"
    #
    # assert actual_result.text == expected_result, f'Expected {expected_result} but got {actual_result.text}'
    # print("Test Case passed")
    context.app.checkout_page.cart_empty_message()

@then("Verify the products")
def number_and_price_of_products(context):
    sleep(5)
    # items = context.driver.find_element(*cart).text
    # expected_result = '1 item'
    # print(items)
    # assert expected_result in items, f'{expected_result} =! {items}'
    context.app.checkout_page.verify_product()
