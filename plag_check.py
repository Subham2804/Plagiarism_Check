from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import random
import string
import time


text = input("Enter the text you want to check: ")


driver = webdriver.Chrome()
driver.get('https://smallseotools.com/plagiarism-checker/')
textbox = driver.find_element_by_name("txt2check")
textbox.send_keys(text)
time.sleep(10)
submitbutton = driver.find_element_by_class_name(
    "check_resbtn")
submitbutton.click()
print("Please pass reCAPTCHA within 60 seconds")
time.sleep(60)
plagarism = driver.find_element_by_id("plagiarizeCount").text
if(plagarism):
    print("Plagarism found")
    print(plagarism)
tab = driver.find_element_by_class_name("tab_image_msr")
tab.click()

source = driver.find_element_by_class_name("web_title_ms")
print("Source matched")
print(source.text)
time.sleep(100)
driver.close()
