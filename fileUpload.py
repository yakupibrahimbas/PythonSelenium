from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)


selectfile=driver.find_element(By.ID,"file-upload").click()
file=".\dropdown.py"
selectfile.send_keys(file)
time.sleep(3)

upload=driver.find_element(By.ID,"file-submit")
WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located(By.TAG_NAME,"h3"))
baslik=driver.find_element(By.TAG_NAME,"h3").text
print(baslik)
dosya=driver.find_element(By.ID,"uploaded-filess").text
print(dosya)
