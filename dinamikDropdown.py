from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://ucuzabilet.com")
nereden=driver.find_element(By.ID,"from_text")
time.sleep(3)
nereden.send_keys("avust")
time.sleep(3)
graz=driver.find_element(By.XPATH,"//li[contains(text(), 'GRZ')]")
graz.click()
time.sleep(3)
