from selenium import webdriver
from time import sleep 
drive = webdriver.chrome(executable_path="C:\Users\hoosi\Downloads\chromedriver_win32 (1)")
driver.get("https://instagram.com")
sleep(4)
driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
    .send_keys(("put you username here!!!!"))
driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
    .send_keys(("put you password here!!!!"))
driver.find_element_by_xpath(('/button[@type="submit'))\
    .click()
sleep(3)                        