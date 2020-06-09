from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import http.client
import urllib.request
import datetime

today = datetime.datetime.now()
todayDate = today.strftime("20%y%m%d")
b7Date = eval(todayDate)-8

#open_url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + open_api_key + params
data = []

def getCoronaData():
    open_api_key = 'S8rzdkL5i25h2g%2Bk0QgRu%2B4GJ8ShKEiyJAR1xCDbaOj%2Ffh2BCT04Om0AKgQx4mSH1Cu%2BK3GOIB2GwivyW%2B1FSg%3D%3D'

    open_url =f"http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey={open_api_key}&pageNo=1&numOfRows=10&startCreateDt={b7Date}&endCreateDt={todayDate}&"

    html = urlopen(open_url).read()
    soup = BeautifulSoup(html,'html.parser')

    rc= soup.select('resultcode')
    resultcode = rc[0].text

    # de = soup.select('stateDt')
    # date = de[0].text
    # if (date != todayDate):
    #     b7Date = b9Date

    #안열리는 오류가 발생하여 오류 없이 열동안 반복
    while resultcode != '00':
        html = urlopen(open_url).read()
        soup = BeautifulSoup(html, 'html.parser')

        rc = soup.select('resultcode')
        resultcode = rc[0].text

    soups = soup.select('item')


    for i in soups:
        #누적검사진행수
        accExamCnt = i.select('accExamCnt')
        totalExam = accExamCnt[0].text

        #누적검사완료수
        accExamCompCnt = i.select('accExamCompCnt')
        doneExam =accExamCompCnt[0].text

        #치료중인 환자수0
        careCnt = i.select('careCnt')
        care =careCnt[0].text

        #격리해재 수0
        clearCnt = i.select('clearCnt')
        clear =clearCnt[0].text

        #사망자 수0
        deathCnt = i.select('deathCnt')
        death = deathCnt[0].text

        #확진자 수0
        decideCnt = i.select('decideCnt')
        getCorona = decideCnt[0].text

        #검사진행 수0
        examCnt = i.select('examCnt')
        exam = examCnt[0].text

        #결과 음성수0
        resutlNegCnt = i.select('resutlNegCnt')
        resutlNeg = examCnt[0].text

        #날짜0
        stateDt = i.select('stateDt')
        date = stateDt[0].text
        #날짜, 확진자 수, 사망자 수, 치료중인환자 수, 검사진행 수, 완치자 수, 결과 음성수, 누적검사완료 수, 누적 검사 수
        temp = {'date':date, 'getCorona':getCorona,'death':death,'care':care,
                'exam':exam,'clear':clear,'resutlNeg':resutlNeg,'doneExam':doneExam,'totalExam':totalExam }
        data.append(temp)

    print("코로나데이터 파싱완료")

getCoronaData()

