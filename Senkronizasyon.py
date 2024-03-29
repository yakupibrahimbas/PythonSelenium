from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://pynishant.github.io/Selenium-python-waits.html")
time.sleep(3)
tryit=driver.find_element(By.XPATH,"//button").click()
WebDriverWait(driver,45).until(expected_conditions.presence_of_element_located(By.ID,"waitCreate"))

clickme=driver.find_element(By.ID,"waitCreate").click()
time.sleep(60)

#implicit wait -gizli bekleme
#explicit wait- aciktan bekleme
