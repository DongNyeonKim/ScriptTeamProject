# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# # Chrome 웹 드라이버 생성
# driver = webdriver.Chrome('D:/chromedriver.exe')
#
# # url 로딩
# driver.get('https://search.naver.com/search.naver?query=%EA%B5%AD%EB%82%B4+%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty')
#
# # # 검색창 검색
# # #elem = driver.find_element_by_id("query")
# # elem = driver.find_element_by_name("query")
# # elem.send_keys("국내 코로나")
# #
# # elem = driver.find_element_by_class_name("button")
# # elem.click()

#from urllib import Request, urlopen
#from urllib import urlencode, quote_plus

from urllib.parse   import quote
from urllib.request import urlopen

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
queryParams = '?' +urlencode({quote_plus('ServiceKey') : '서비스키',quote_plus('ServiceKey') : '-',quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('startCreateDt') : '20200310', quote_plus('endCreateDt') : '20200315' })

request =Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body =urlopen(request).read()
print (response_body)
