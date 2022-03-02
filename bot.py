#from lib2to3.pgen2 import driver
from selenium import webdriver
import time
import os, time

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

driver.get('https://web.whatsapp.com/')
time.sleep(10)

celular = "cellphoneNumber"  #  Destination cellphoneNumber
mensaje = "Message"  # Message to send

driver.get("https://wa.me/" + celular + "/?text=" + mensaje)
time.sleep(5)

btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(5)
btn = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
btn.click()
time.sleep(30)

# Btn                                //*[@id='main']/footer/div[1]/div[3]")[0]         
btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
btn.click()
time.sleep(5)

print("Fin del programa")

driver.close()