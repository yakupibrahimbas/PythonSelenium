from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
import time
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app")
time.sleep(5)
def siparisver():
    driver.find_element(By.ID,"siparis").click()
def mesajOku():
    return driver.find_element(By.ID,"mesaj").text
siparisver()
mesaj=mesajOku()
assert mesaj=="Musteri ismi girmediniz"
isim="Tom Cruise"
driver.find_element(By.ID,"musteri-adi").send_keys(isim)
siparisver()
mesaj=mesajOku()
assert mesaj=="Pizza boyu seçmediniz"
driver.find_element(By.CSS_SELECTOR,"input[value='Küçük']").click()
siparisver()
mesaj=mesajOku()
assert mesaj=="Ödeme tipi seçmediniz"
zeytin=driver.find_element(By.CSS_SELECTOR,"input")

dropdown=driver.find_element(By.ID,"odeme-tipi")
odeme=Select(dropdown)
odeme.select_by_index(2)
siparisver()
mesaj=mesajOku()
assert mesaj=="Siparişiniz alındı"

musteri=driver.find_element(By.ID,"musteri").text
boy=driver.find_element(By.ID,"pizzaboyu").text
ek=driver.find_element(By.ID,"odeme").text
odeme=driver.find_element(By.ID,"odeme").text
tutar=driver.find_element(By.ID,"tutar").text

assert musteri=="Musteri ismi:"+isim
assert boy=="Pizza boyu: Küçük"
assert ek=="Pizza üstü:"
assert odeme=="Ödeme tipi:Kredi Kartı"
assert tutar=="Tutar:10 TL"


