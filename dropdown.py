from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://mynet.com")
time.sleep(5)

driver.execute_script("window.scrollBy(0,1250)","")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-500)","")
time.sleep(5)

driver.save_screenshot("./scrolll.png")
time.sleep(5)