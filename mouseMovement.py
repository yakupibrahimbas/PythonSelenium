from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://the-internet.herokuapp.com/hovers")
time.sleep(3)
user=driver.find_element(By.CSS_SELECTOR,"div.figure")
isim=driver.find_element(By.CSS_SELECTOR,"div.figcaption h5")
link=driver.find_element(By.CSS_SELECTOR,"div.figcaption a")

time.sleep(3)

hareket=ActionChains(driver)
hareket.move_to_element(user)
hareket.move_to_element(isim)
hareket.move_to_element(link)
hareket.perform()
time.sleep(3)
print(user.is_displayed())
print("isim:"+isim.text)
link.click()
time.sleep(5)