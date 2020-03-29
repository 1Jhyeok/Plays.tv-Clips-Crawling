import re
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def download(url, title):
    #1 Windows 파일명 규칙에 어긋나는 특수문자들
    pattern = r"[\\/\:\*\?\"\<\>\|]"

    #2 패턴에 따라 특수문자 제외
    title = re.sub(pattern, '', title)

    #3 파일 다운로드
    urllib.request.urlretrieve(url, "mp4\\" + title + ".mp4")
    print(title + ' Done!')

def getUrls(html):
    soup = BeautifulSoup(html, "lxml")


    videoUrls = []
    titles = []

    for link in soup.find("div", class_="video-list-container").find_all("div", class_="info"):
        str = "https://web.archive.org" + link.find("a")["href"]
        videoUrls.append(re.sub('\?.*', '', str))        

    for url in videoUrls:
        print("URL: " + url)

        req = urllib.request.Request(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, "lxml")
        description = soup.find("span", class_="description-text")
        titles = description.text

        print("Title: " + titles)

        video = soup.find("source")
        mp4 = "http:" + video['src']
        download(url, mp4)     

def main():
    username = input("Input your plays.tv's username: ")

    browser = webdriver.Chrome()
    browser.implicitly_wait(3)

    url = 'https://web.archive.org/web/https://plays.tv/u/' + username
    browser.get(url)

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(3.5)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html = browser.page_source
    getUrls(html)


main()