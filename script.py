from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

TARGET = "notes and ss" #Full Name of group or person you want to spam
SPAM = "Hello LinkedIn" #The text you want to spam
TIMES = 10 #Times you want to spam

PATH = "/Users/mac/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://web.whatsapp.com")
print("WhatsApp Web loaded! You have 15 seconds to scan QR code!")
time.sleep(15)

search = driver.find_element_by_class_name("_3FRCZ")
search.send_keys(TARGET)
search.send_keys(Keys.RETURN)

print('Target acquired')
time.sleep(2)

print("Starting spam")
input = driver.find_element_by_class_name("_3uMse")

for i in range(TIMES):
    input.send_keys(SPAM)
    time.sleep(0.02)
    input.send_keys(Keys.RETURN)
    print("Spammed", i, "times")

print("Quitting...")
time.sleep(5)

driver.quit()