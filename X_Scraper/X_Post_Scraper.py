import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()

url = "https://x.com/ABrownBeing/status/1827381444894949685"

driver.get(url)

texts = driver.title 

i = 0 

id = " "

post = " "

for text in texts:
    if text=="X":
        i = 1 
    if text == ":" or text == " / " or text == "on":
        pass
    if i == 0 : 
        id+=text
    elif i == 1 and text != "X":
        post+=text
         

# print(driver.title)
id.strip()

post.strip()

print(id)
print(post)
driver.quit()