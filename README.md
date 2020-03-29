# Plays.tv Clips Crawling

# 왜 만들었는가?
입대했는데 그 사이 서비스가 중단되어서 클립을 다운받지 못하여 만들었습니다.

# 어떻게 사용하는가?
파이썬을 [다운로드](https://www.python.org/downloads/)해주세요.(파이썬 3.8 사용)

크롬브라우저의 버전에 맞는 크롬드라이버를 [다운로드](https://chromedriver.chromium.org/downloads)하여 파이썬 파일과 동일한 경로에 위치해주세요.

pip install selenium, pip install bs4 를 하여 셀레니움과 bs4를 설치해주세요.

실행하고 나서 Plays의 닉네임을 입력해주세요.

그러면 브라우저가 열리고 최하단까지 스크롤합니다.

그 후 실행파일의 위치에서 mp4폴더가 생기고 순차적으로 다운로드 됩니다.
