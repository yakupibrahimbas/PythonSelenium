from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://google.com")
time.sleep(5)
print(driver.current_window_handle)
driver.switch_to.new_window("tab")
driver.get("https://tesla.com")
time.sleep(5)
print(driver.current_window_handle)
print(driver.window_handles)
time.sleep(5)