#크롤링

# import urllib.request
# from bs4 import BeautifulSoup

# url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98'
# #url을 받아오기
# html = urllib.request.urlopen(url).read()
# #url을 분석
# soup = BeautifulSoup(html, 'html.parser')

# title = soup.find_all(class_='sh_blog_title')

# for i in title:
#     print(i.attrs['title'])
#     print(i.attrs['href'])
#     print()



import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
#한글 변환

baseURL ='https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusURL = input("검색어를 입력하세요:")

url = baseURL + urllib.parse.quote_plus(plusURL)
#한글 변환시켜주는것    urllib.parse.quote_plus
    #영어는 그대로 영어로 변환을 시켜야할 URL만 html로 사용하도록 변환함

#print(url)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()