from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")
time.sleep(5)
dropdown=driver.find_element(By.ID,"odeme-tipi")
odeme=Select(dropdown)
odemeTipleri=odeme.options

for tip in odemeTipleri:
    print(tip.text)
odeme.select_by_visible_text("Kredi Kartı")
time.sleep(3)
odeme.select_by_index(3)
time.sleep(3)
