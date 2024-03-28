from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
#driver.get("https://the-internet.herokuapp.com/login")
#driver.maximize_window()
##//*[@name='username']
##//*[@name='password']
##//button
#kullaniciAdi=driver.find_element(By.XPATH,"//*[@name='username']").send_keys("tomsmith")
#time.sleep(5)
#password=driver.find_element(By.XPATH,"//*[@name='password']").send_keys("SuperSecretPassword!")
#time.sleep(5)
#button=driver.find_element(By.XPATH,"//button").click()
#time.sleep(5)
#logout=driver.find_element(By.XPATH,"//*[@href='/logout']").click()
#time.sleep(5)
#if "login" in driver.current_url:
#    print("OK.Login sayfasina donduk")
#else:
#    print("HATA:login sayfasina donmedi")
#basariliIslem=driver.find_element(By.ID,"flash").is_displayed()

def login(username,password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.XPATH, "//*[@name='username']").send_keys(username)
    driver.find_element(By.XPATH, "//*[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button").click()
login("adada","fsfsf")