from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Chrome 웹 드라이버 생성
driver = webdriver.Chrome('D:/chromedriver.exe')

# url 로딩
driver.get('https://search.naver.com/search.naver?query=%EA%B5%AD%EB%82%B4+%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty')

# # 검색창 검색
# #elem = driver.find_element_by_id("query")
# elem = driver.find_element_by_name("query")
# elem.send_keys("국내 코로나")
#
# elem = driver.find_element_by_class_name("button")
# elem.click()