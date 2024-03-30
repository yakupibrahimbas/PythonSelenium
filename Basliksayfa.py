from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://tomspizzeria.herokuapp.com/yeni-sekme.html")
time.sleep(5)