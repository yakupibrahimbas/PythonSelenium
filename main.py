from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
link=driver.current_url
baslik=driver.title
print(("Sayfaaa basligi:"+baslik))

print("suanki baslik"+link)
if "google.com" in link:
    print("Dogru google sayfasindayiz."+link)
else:
    print("yanlis google sayfasindasiniz")

driver.maximize_window()
driver.get("https://etsy.com")
link=driver.current_url
baslik=driver.title
print(("Sayfaaa basligi:"+baslik))
driver.save_screenshot("./ekrangoruntusu.png")
if "etsy.com" in baslik:
    print("Dogru etsy sayfasindayiz"+link)

driver.back()

baslik=driver.title
if "Google" in baslik:
    print("Tebrikler")
driver.save_screenshot("./Googleekrangoruntusu.png")

print("suanki baslik"+link)
#driver.close() #suanki pencereyi kapatir
#driver.quit() #tum pencereleri kapatir /Testler cok oldugunda bircok pencere calisacagi icin idealdir


