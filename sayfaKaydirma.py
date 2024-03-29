from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://www.lovehomeswap.com")
time.sleep(3)
driver.execute_script("window.scrollBy(0,750)","")
time.sleep(3)
istanbul=driver.find_element(By.XPATH,"(//h2)[3]")
time.sleep(3)
driver.execute_script("arguments[0].scrollIntoView()",istanbul)
time.sleep(3)
