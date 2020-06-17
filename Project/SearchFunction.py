import webbrowser as wbs

def getCoronanews():
    wbs.open('https://search.naver.com/search.naver?query=%EA%B5%AD%EB%82%B4+%EC%BD%94%EB%A1%9C%EB%82%98&where=news&ie=utf8&sm=nws_hty', new=1)

def getScreeningClinic():
    wbs.open('https://www.mohw.go.kr/react/popup_200128_3.html', new=1)


def getScreeningCarClinic():
    wbs.open('https://www.mohw.go.kr/react/popup_200128_4.html', new=1)

def getSafetyHospital():
    wbs.open('https://www.mohw.go.kr/react/popup_200128.html', new=1)