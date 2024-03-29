from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")
time.sleep(5)
ortaBoyPizza=driver.find_element(By.XPATH,"//*[@value='Orta']")
zeytin=driver.find_element(By.XPATH,"//*[@value='zeytin']")
mantar=driver.find_element(By.XPATH,"//*[@value='mantar']")
print(ortaBoyPizza.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
time.sleep(5)

ortaBoyPizza.click()
zeytin.click()
mantar.click()
time.sleep(5)
print(ortaBoyPizza.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())