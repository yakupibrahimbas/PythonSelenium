from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
option=Options()
option.add_argument()
import time
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://google.com")