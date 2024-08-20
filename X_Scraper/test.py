
from selenium import webdriver
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


from X_Image_Scraper import X_Picture

if __name__ == '__main__' :
    pic_link = 'https://x.com/FabrizioRomano/status/1825513124918677856/photo/1'

    pic = X_Picture(pic_link)

    pic.get_X_picture()