from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
driver.maximize_window()

seckinMadde=driver.find_element(By.ID,"mp-tfa")
seckinMaddeText=seckinMadde.text
seckinMaddeText=seckinMaddeText.split(",")[0]
print(seckinMaddeText)
kaliteli_madde=driver.find_element(By.ID,"mf-tfp").text
kaliteli_madde=kaliteli_madde.split(",")[0]
print(kaliteli_madde)
time.sleep(5)

