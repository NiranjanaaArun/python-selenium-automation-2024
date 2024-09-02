from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
sleep(2)
search_button = driver.find_element(By.ID,'search')
search_button.send_keys('tea')
driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(10)

actual_result = driver.find_element(By.XPATH, "//div[@class='sc-f82024d1-0 NQtvb']").text
expected_result = "tea"

assert expected_result in actual_result
print("Test Case passed")




