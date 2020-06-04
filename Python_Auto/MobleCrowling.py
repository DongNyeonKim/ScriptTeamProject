import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# api_txt_lines total_tit

search = input('검색어를 입력하세요:')
url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'
html = urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

total = soup.select('.api_txt_lines.total_tit')

searchList = []


for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)

f = open(f'{search}.csv','w', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)

f.close()

print('Done!!')

