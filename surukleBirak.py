from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/droppable/")
time.sleep(3)
kaynak=driver.find_element(By.CSS_SELECTOR,"div#simpleDropContainer div")
hedef=driver.find_element(By.XPATH,"(//*[.='Drop here'])[1]")
print(kaynak.text)
print(hedef.text)

action=ActionChains()
action.drag_and_drop(kaynak,hedef).perform()
time.sleep(10)