from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
#buton1=driver.find_element(By.XPATH,"//*[@onclick='jsAlert()']")
#buton1.click()
#WebDriverWait(driver,3).until(expected_conditions.alert_is_present())
#alert=Alert(driver)
#time.sleep(2)
#mesaj=alert.dismiss()
#alert.dismiss()
#print(driver.find_element(By.ID,"result")).text
#
#
#time.sleep(50)
#buton2=driver.find_element(By.XPATH,"//*[@onclick='jsConfirm()']")
buton3=driver.find_element(By.XPATH,"//*[@onclick='jsPrompt()']")
buton3.click()
alert=Alert(driver)
time.sleep(2)
alert.send_keys("selenium alert test")
alert.accept()
time.sleep(5)
