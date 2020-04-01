import re
import os
import errno
import itertools
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError, URLError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

def download(url, title):
    #3 파일 다운로드
    filename = "mp4\\" + title + ".mp4"
    urlretrieve(url, filename)    
    print(title + ' Done!')

def getUrls(html):
    soup = BeautifulSoup(html, "lxml")


    videoUrls = []
    titles = []
    errcnt = 0

    #1 각 비디오 링크 추출
    for link in soup.find("div", class_="mod mod-user-videos activity-feed inited").find_all("div", class_="info"):
        str = "https://web.archive.org/web/https://plays.tv" + link.find("a")["href"]
        #2 더미 파라미터 제거
        videoUrls.append(re.sub(r"\?.*", '', str))

        #3 제목 추출
        str = link.find("a", class_="title")
        titles.append(str.text)
    
    for (url, title) in zip(videoUrls, titles):
        print("URL: " + url)
        filename = "mp4//" + title + ".mp4"

        if not os.path.exists(filename):
            try:
                sourcecode = urlopen(url).read()
            except HTTPError as e:
                print("Title: " + title + " is HTTP Error Skip")
                errcnt + 1
                continue

            soup = BeautifulSoup(sourcecode, "lxml")
            video = soup.find("source")
            mp4 = "http:" + video['src']

            #1 Windows 파일명 규칙에 어긋나는 특수문자들
            pattern = r"[\\/\:\*\?\"\<\>\|]"

            #2 패턴에 따라 특수문자 제외
            title = re.sub(pattern, '', title)

            #3 상대경로에 mp4/{title}.mp4 로 저장됨
            download(mp4, title)
        else:
            print("Title: " + title + " is Exist, skip!")

    
    print("Total: " + str(len(titles)))
    print("Error: " + str(errcnt))

def main():
    username = input("Input your Plays.tv's Username: ")

    url = 'https://web.archive.org/web/https://plays.tv/u/' + username

    
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)

    browser.get(url)

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    # 맨 밑으로 계속 스크롤
    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(5)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 전체 페이지 html 소스
    html = browser.page_source

    getUrls(html)
    browser.close()
    print("Done !")


main()