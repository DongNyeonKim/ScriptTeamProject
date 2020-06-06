from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import http.client
import urllib.request

#open_url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + open_api_key + params


open_api_key = 'S8rzdkL5i25h2g%2Bk0QgRu%2B4GJ8ShKEiyJAR1xCDbaOj%2Ffh2BCT04Om0AKgQx4mSH1Cu%2BK3GOIB2GwivyW%2B1FSg%3D%3D'
params = '&pageNo=1&numOfRows=10&startCreateDt=20200601&endCreateDt=20200606&'

open_url ="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=S8rzdkL5i25h2g%2Bk0QgRu%2B4GJ8ShKEiyJAR1xCDbaOj%2Ffh2BCT04Om0AKgQx4mSH1Cu%2BK3GOIB2GwivyW%2B1FSg%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200601&endCreateDt=20200606&"

request = urllib.request.Request(open_url)

response = urllib.request.urlopen(request)
rescode = response.getcode()

print(rescode)
# resultCode = soup.select('resultCode')
#
# if resultCode == '00':
#     print(resultCode)


# total = soup.select('._2TFfLkGZhc')
#
# SearchList = []
#
# ##
# num=1
#
# for i in total:
#     temp = []
#     tagname = search+str(num)
#     names = i.select('._3ldP-RMmbZ')
#     name = names[0].text
#     prices = i.select('._1vPmSw6Psr')
#     price = prices[0].find("strong").text + '원'
#     url = soup.select('._1SwezRSbBH > a')[0]['href']
#
#     num += 1
#     temp.append(tagname)
#     temp.append(name)
#     temp.append(price)
#     temp.append(url)
#     SearchList.append(temp)
#
