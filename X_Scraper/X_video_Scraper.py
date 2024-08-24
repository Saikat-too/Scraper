import requests 

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import os 
import m3u8

url = "https://x.com/oshinosakii/status/1826667221957140798"

driver = webdriver.Firefox()

driver.get(url)

JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
network_requests = driver.execute_script(JS_get_network_requests)

for n in network_requests:
    if "master.m3u8" in n["name"]:
        url = n["name"]
        
        
r = requests.get(url)

m3u8_master = m3u8.loads(r.text)

print(m3u8_master)

playlist_url = m3u8_master.data["playlists"]['uri']

r = requests.get(playlist_url)

playlist = m3u8.loads(r.text)

r = requests.get(playlist_url)

with open ('videos.ts' , 'wb') as f:
    for segment in playlist.data['segments']:
        url = segment['uri']
        r = requests.get(url)
        
        f.write(r.content)
        
os.remove("video.ts")
os.remove("audio.ts")
os.remove("output.ts")

