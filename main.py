from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Mesajları mesaj.txt dosyasından al
with open('message.txt', 'r', encoding='utf-8') as messages:
    messageList = messages.read().splitlines()

def wait_for_qr_scan(driver):
    print("Lütfen QR kodunu taratın...")
    while "Loading" in driver.title:  # Sayfa başlığı değiştiğinde giriş yapılmış demektir
        time.sleep(1)
    print("QR kod başarıyla tarandı!")

def start():
    driver = webdriver.Chrome()  # Selenium driver'ı başlat
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')  # WhatsApp Web aç
    wait_for_qr_scan(driver)  # QR kod taramasını bekle

    # Mesaj gönderme işlemi
    while True:
        for message in messageList:
            try:
                message_area = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
                message_area.send_keys(message)  # Mesajı yaz
                message_area.send_keys(Keys.ENTER)  # Enter tuşuna bas
                time.sleep(random.randint(2, 5))  # Mesajlar arasında bekle
            except Exception as e:
                print(f"Hata: {e}")
                break
start()


