from asyncio import Condition

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/register?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Freport%2Finfringement&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_noticeform_desktop_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(2)

Amazon_logo = driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon")
Create_Account_logo= driver.find_element(By.CSS_SELECTOR, "div.a-spacing-small")
Your_name_field= driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
Your_password_field = driver.find_element(By.CSS_SELECTOR, "#ap_password")
min_pass_characters= driver.find_element(By.CSS_SELECTOR, "[class*='alert-inline'][class*='information-messag']")
reenter_password_field = driver.find_element(By.CSS_SELECTOR, "input[id*=ap_password_check]")
create_amazon_account_button= driver.find_element(By.CSS_SELECTOR, "#continue")
Condition_of_use = driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")
Privacy_notice = driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='privacy_notice?ie=UTF8&nodeId=468496']")
sign_in= driver.find_element(By.CSS_SELECTOR, "[href*='/ap/signin?openid.return_to']")
