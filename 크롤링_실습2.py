#selenium : 사람이 웹서핑하는 것처럼(마우스 클릭 등) 코드로 웹서핑할 수 있도록 해줌
#from 라이브러리이름 import 사용할대상이름
from selenium import webdriver  # selenium 라이브러리에서 webdriver 라는 클래스만 사용
                                # 새로운 환경에서 웹 브라우저를 대신해 줄 Web Driver가 필요
                                # Web Driver는 Selenium이 사용할 웹 브라우저
from bs4 import BeautifulSoup as bs #BeautifulSoup를 bs로 지정

path = 'chromedriver.exe'  # 크롬 드라이버 경로 지정
driver = webdriver.Chrome(path)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver(options=options)

search_url = "https://www.melon.com/chart/month/index.htm"
    # search_ur2 = "https://www.mk.co.kr/news/economy/?page={}".format(page)
    # 주소 문자열 따옴표 내에 중괄호{}를 넣어주고, 따옴표 뒤에 .format(page)를 붙여주면,
driver.get(search_url)
driver.implicitly_wait(3) # 사이트가 로딩되도록 3초정도 기다립니다.
soup = bs(driver.page_source, 'html.parser')
# 크롬 드라이버 파일과 같은 폴더에 있다면 같이 파일명만 입력
# 다른 폴더에 있다면 path = 'C:\python\chromedriver.exe' 와 같이 전체 경로를 입력
#driver = webdriver.Chrome(path) # 셀레니움 라이브러리가 크롬 드라이버를 실행합니다.

wow = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
print(wow.text)
print(len(wow))
driver.close()
# # bs4(BeautifulSoup) 라이브러리는 웹사이트의 소스(HTML)를 추출하는 라이브러리입니다.
# # 주로 selenium 라이브러리와 함께 사용됩니다.
# soup = bs(driver.page_source, 'html.parser') 
# wow = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')

# for page in wow:
#         print(page.text)

