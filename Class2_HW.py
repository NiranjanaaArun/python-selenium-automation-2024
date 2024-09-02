from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://na.account.amazon.com/ap/signin?_encoding=UTF8&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.pape.max_auth_age=0&ie=UTF8&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=lwa&openid.assoc_handle=amzn_lwa_na&marketPlaceId=ATVPDKIKX0DER&arb=f9b0139f-2d28-440a-b4d3-c67aa3660267&language=en_GB&openid.return_to=https%3A%2F%2Fna.account.amazon.com%2Fap%2Foa%3FmarketPlaceId%3DATVPDKIKX0DER%26arb%3Df9b0139f-2d28-440a-b4d3-c67aa3660267%26language%3Den_GB&enableGlobalAccountCreation=1&metricIdentifier=amzn1.application.c31a3180b11a4e8d99044bd40865ec65&signedMetricIdentifier=y34KI%2BUaKLdYCtRjxhSc2i')
sleep(2)

Amazon_logo = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
sign_in_button = driver.find_element(By.XPATH,"//div//h1[@class='a-spacing-small']")
email_field = driver.find_element(By.ID, "ap_email")
continue_button= driver.find_element(By.ID, "continue")
conditions_of_use = driver.find_element(By.XPATH, "//a[contains(@href,'agreementName=conditionsOfUse')]")
privacy_notice = driver.find_element(By.XPATH,"//a[contains(@href,'privacyNotice')]")
need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
forgot_password_1 = need_help_link.click()
forgot_password=driver.find_element(By.ID, "auth-fpp-link-bottom")
other_issues_with_signin= driver.find_element(By.ID, "ap-other-signin-issues-link")
create_amazon_account= driver.find_element(By.ID, "createAccountSubmit")

sleep(7)
print("Your locators are all correct")


