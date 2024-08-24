import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()

url = "https://x.com/kareemmpie/status/1827336078551838962"

driver.get(url)

print(driver.title)