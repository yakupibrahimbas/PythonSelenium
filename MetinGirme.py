from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
aramakutusu=driver.find_element(By.ID,"APjFqb")
aramakutusu.send_keys("selenium")
driver.find_element(By.XPATH,"(//*[@class='gNO89b'])[2]").click()
time.sleep(5)


