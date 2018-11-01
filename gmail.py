import pyautogui
from selenium import webdriver
import time
from getpass import getpass

sender_id = input("Enter your email id : ")
password = getpass("Enter your password : ")
recepient_id = input("Enter the email id of user u want to send the mail : ")
subject = input("Subject : ")
content = input("Content : ")


driver = webdriver.Chrome("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver")
driver.get('https://www.google.com/')


driver.find_element_by_xpath(f'//a[text() = "Gmail"]').click()
time.sleep(2)
driver.find_element_by_xpath(f'//a[text() = "Sign In"]').click()
time.sleep(1)
id_box = driver.find_element_by_xpath(f'//input[@type = "email"]')
id_box.send_keys(sender_id)
time.sleep(1)
driver.find_element_by_id('identifierNext').click()
time.sleep(1)
pwd_box = driver.find_element_by_xpath(f'//input[@type = "password"]')
pwd_box.send_keys(password)
time.sleep(1)
driver.find_element_by_id('passwordNext').click()
time.sleep(1)
driver.find_element_by_class_name('z0').click()
time.sleep(1)
driver.find_element_by_id(':q5').send_keys(recepient_id)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
time.sleep(1)
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
time.sleep(1)
driver.find_element_by_id(':pn').send_keys(subject)
time.sleep(1)
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
time.sleep(1)
driver.find_element_by_id(':qs').send_keys(content)
time.sleep(1)
driver.find_element_by_id(':pd').click()

