from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://imdb.com/")
driver.find_element(By.XPATH,"//*[@class='ipc-responsive-button__text']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Top 250 Movies']").click()
time.sleep(5)
film_isimleri=driver.find_elements(By.XPATH,"//h3")
for i in range(250):
    print(film_isimleri[i].text)
time.sleep(60)
