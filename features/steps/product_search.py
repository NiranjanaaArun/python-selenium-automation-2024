from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')

SEARCH_WORD=(By.ID, 'search')
SELECTED_SIZE = (By.CSS_SELECTOR, "div[data-test='@web/VariationComponent'] li[data-io-i='1']")
ALL_COLORS = (By.CSS_SELECTOR, "div[data-test='@web/VariationComponent']:nth-of-type(2) li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div[data-test='@web/VariationComponent']:nth-of-type(2)")


LISTINGS= (By.CSS_SELECTOR, "div[data-test*='site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test*='product-title']")
PRODUCT_IMG= (By.CSS_SELECTOR, "picture[data-test='@web/ProductCard/ProductCardImage/primary'] img")

@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')

@given('Open target product {product_id} page')
def open_target_product(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)

# @given('Open Target page')
# def open_target(context):
#     # context.driver.get('https://www.target.com/')
#     context.app.main_page.open_main()

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)

@when('Input {search_word} into search field1')
def word(context, search_word):
    # search= context.driver.find_element(*SEARCH_WORD)
    # search.send_keys(search_word)
    # context.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    context.app.header.search_product(search_word)

@when('Search for an {item}')
def item_search(context, item):
    # search_tab = context.driver.find_element(By.ID, 'search')
    # search_tab.send_keys(item)
    # context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    context.app.header.search_product(item)
    sleep(10)

@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):

    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'

@then('Verify {search_word} is on the search results header')
def results_header(context, search_word):
    context.app.search_results_page.verify_results_header(search_word)

@then('Verify user can click through colors')
def verify_colors(context):

    context.driver.find_element(*SELECTED_SIZE).click()

    expected_result = ['grey', 'navy/tan', 'stone/grey', 'white/sand/tan', 'dark khaki','white/navy/red']
    actual_result = []

    all_colors = context.driver.find_elements(*ALL_COLORS)
    print(all_colors)

    for color in all_colors:
        print(color)
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)
        selected_color = selected_color.split('\n')[1]
        actual_result.append(selected_color)
        print(actual_result)

    assert actual_result == expected_result, f'{actual_result} is not {expected_result}'


@then('Verify product name and product image')
def verify_name(context):

    context.driver.execute_script("window.scrollBy(0, 1000)","")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 1000)","")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 1000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 1000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 1000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 1000)", "")
    all_products= context.driver.find_elements(*LISTINGS)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        # assert title, 'Product title not shown'
        # print(title)
        img = product.find_element(*PRODUCT_IMG)
        print(img)



