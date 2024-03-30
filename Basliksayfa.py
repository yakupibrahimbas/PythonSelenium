from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://techproeducation.com/")
#anasayfa=driver.current_window_handle
time.sleep(5)

programs=driver.find_element(By.ID,"(//*[.='Programs'])[1]").click()
events=driver.find_element(By.ID,"(//*[.='Events'])[1]").click()
blog=driver.find_element(By.ID,"(//*[.='Blog'])[1]").click()

def sekme_degistir(baslik):
    for sayfa in driver.window_handles:
        driver.switch_to.window(sayfa)
        if baslik in driver.title:
            break;

time.sleep(5)

anasayfa=driver.window_handles[0]
programs=driver.window_handles[1]
events=driver.window_handles[2]
blog=driver.window_handles[3]

time.sleep(5)

driver.switch_to.window(programs)
print("programs:"+driver.title)

time.sleep(3)


driver.switch_to.window(events)
print("events:"+driver.title)

time.sleep(3)


driver.switch_to.window(blog)
print("blog:"+driver.title)
