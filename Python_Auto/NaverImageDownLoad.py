from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseURL = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusURL = input('검색어를 입력하세요:')

url = baseURL+ quote_plus(plusURL)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

img = soup.find_all(class_='_img')

print(len(img))

n = 1

for i in img:
    imgURL = (i['data-source'])
    with urlopen(imgURL) as f:
        with open(plusURL + str(n)+ '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1

print('다운로드 완료')