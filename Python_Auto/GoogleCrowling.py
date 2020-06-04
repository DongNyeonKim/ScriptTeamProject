from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseURL = 'https://www.google.com/search?q='
plusURL = input('검색어를 입력하시오:')
url = baseURL + quote_plus(plusURL)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

r = soup.select('.r')

# print(type(r))

for i in r:
    # print(i.select_one('.ellip').text)
    # print(i.select_one('.iUh30.bc').text)
    print(i.a.attrs['href'])
    print()

driver.close()