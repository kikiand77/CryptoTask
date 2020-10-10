# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:35:46 2020

@author: dell
"""

from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.fullscreen_window()

driver.get("https://crypto.com/exchange")

# Locate CMO Markets and click
time.sleep(10)
driver.find_elements_by_class_name("e-tabs__nav-item")[2].click()
time.sleep(10)
# Locate CRO/USDC and click Trade button
element = driver.find_elements_by_class_name("home-tbody-li").pop()
button = element.find_elements_by_xpath("//button[@class='trade-btn e-button e-button--primary e-button--medium']")
num=len(button) - 1
driver.execute_script("arguments[0].click();", button[num])

# Jump to login page 
driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()

#driver.get("https://auth.crypto.com/users/sign_in")
email = driver.find_element_by_xpath("//input[@type='email']")
pwd = driver.find_element_by_xpath("//input[@type='password']")
submit = driver.find_element_by_xpath("//input[@type='submit']")

#test case 1: enter valid email and password
email.send_keys("email@gmail.com")
pwd.send_keys("12345Qa!")
submit.click()
