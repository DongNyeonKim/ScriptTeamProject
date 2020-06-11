from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Chrome 웹 드라이버 생성

def getCoronanews():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://search.naver.com/search.naver?query=%EA%B5%AD%EB%82%B4+%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty')

def getScreeningClinic():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.mohw.go.kr/react/popup_200128_3.html')


def getScreeningCarClinic():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.mohw.go.kr/react/popup_200128_4.html')

def getSafetyHospital():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.mohw.go.kr/react/popup_200128.html')