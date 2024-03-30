from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://techproeducation.com/")
#anasayfa=driver.current_window_handle
frameler=driver.find_element(By.TAG_NAME,"iframe")
print(frameler)