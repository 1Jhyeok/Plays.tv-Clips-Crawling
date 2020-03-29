from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
browser.implicitly_wait(3)


# username = input("Input your plays.tv's username: ")
username = "yeonstar" # It's Debug Please Delete Me 삭제요망!!
url = 'https://web.archive.org/web/https://plays.tv/u/' + username
browser.get(url)

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

