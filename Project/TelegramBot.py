import time
import telepot
from CoronaStateXMLParsing import data
import requests
from tqdm import tqdm

token = "1285432386:AAF_04K0iMDFYSMFf9v8r0rUUzfEpR4Ptl0"
bot = telepot.Bot(token)

def handle(msg):
    global chat_id
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg)
    print(msg['text'])
    #print(content_type, chat_type, chat_id)


    if "안녕" in msg['text']:
        bot.sendMessage(chat_id, "안녕하세요 "+(msg['from']['first_name'])+" "+(msg['from']['last_name'])+"님 "+ "\n코로나종합상황센터입니다. 무엇을 도와드릴까요?")
    elif ("안내" in msg['text']) or ("기능" in msg['text']):
        giveInfo()
    elif "뭐해" in msg['text']:
        bot.sendMessage(chat_id, "명령을 기다리고 있어요!")
        bot.sendSticker(chat_id, "https://lh3.googleusercontent.com/proxy/suFcndokrjSE6hVmSX578SyIiZrp7JRM-ezpYCRqTeVicMonfjaljYZU6RQkKz2C3kpGUTMjKCkPe06UQxPRS64x117tJzgoZ7_p6JtULF9DB56b0R2Uu1uLyUDNnRSHp7r1Op8hUqHt5Gf9zL21m11kz4q2LrJ7HhTN_JPGUFyxMRAgqbsl--ushg")
    elif ("금일"in msg['text'] or "오늘" in msg['text']) and ("감염"in msg['text'] or "확진자" in msg['text']):
        giveTodayCoronaState()
    elif ("전일" in msg['text'] or "어제" in msg['text']) and ("감염"in msg['text'] or "확진자" in msg['text']):
        giveYesterdayCoronaState()
    elif ("공적"in msg['text'] and "마스크" in msg['text']):
        giveMaskInfo(msg['text'])
    else:
        bot.sendMessage(chat_id, "다시한번말해주세요 이해를 못했어요!")

bot.message_loop(handle)

def getNearMaskStoreInfo(address):
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=" + requests.utils.unquote(address)

    req = requests.get(url)

    json_data = req.json()
    store_data = json_data['stores']

    MaskList=[]
    for i in tqdm(range(len(store_data))):
        addrs=(store_data[i]['addr'])
        codes=(store_data[i]['code'])
        latitudes=(store_data[i]['lat'])
        longitudes=(store_data[i]['lng'])
        names=(store_data[i]['name'])
        types=(store_data[i]['type'])
        try:
            created_ats=(store_data[i]['created_at'])
        except:
            created_ats=("no_data")
        try:
            remain_stats=(store_data[i]['remain_stat'])
        except:
            remain_stats=("no_data")
        try:
            stock_ats=(store_data[i]['stock_at'])
        except: stock_ats=("no_data")
        if remain_stats=="plenty":
            remain_stats="100개 이상"
        if remain_stats == "some":
            remain_stats = "30개 이상 100개 미만"
        if remain_stats == "few":
            remain_stats = "2개 이상 30개 미만"
        if remain_stats == "empty":
            remain_stats = "1개 이하"
        if remain_stats == "break":
            remain_stats = "판매중지"
        if remain_stats == "no_data":
            remain_stats = "데이터 없음"

        maskproduct = [{"addr": addrs, "code": codes, "latitude": latitudes, "longitude": longitudes, "name": names,
                       "type": types, "created_at": created_ats, "remain_stat": remain_stats, "stock_at": stock_ats}]
        MaskList.append(maskproduct)

    #print(len(addrs), len(codes), len(latitudes), len(longitudes), len(names), len(types), len(created_ats), len(remain_stats), len(stock_ats))


    return MaskList

def giveMaskInfo(text):
    command, address = text.split(":")
    MaskList = getNearMaskStoreInfo(address)
    print(MaskList)

    text = f'''
{address}의 공적마스크 판매처 및 제고량 안내입니다.
            '''
    bot.sendMessage(chat_id, text)

    for i in range(len(MaskList)):
        mapAddress = MaskList[i][0]["addr"].replace(" ","+")
        text = f'''
판매처 이름 : {MaskList[i][0]["name"]}\n
주소 : {MaskList[i][0]["addr"]}\n
제고량 : {MaskList[i][0]["remain_stat"]}\n
데이터 생성일자 : {MaskList[i][0]["created_at"]}\n
입고시간 : {MaskList[i][0]["stock_at"]}\n
지도 : https://www.google.co.kr/maps/place/{mapAddress}\n
                    '''
        bot.sendMessage(chat_id, text)

    text = f'''
{address}에 {len(MaskList)}개의 공적마스크 판매처가 있습니다.\n
감사합니다.
                '''
    bot.sendMessage(chat_id, text)


def giveInfo():
    text = f'''
기본 의사소통 : 안녕, 뭐해?\n
코로나 감염현황 확인 : 오늘(금일), 전일(어제), 확진자(감염)\n
위 문자들을 입력하세요!!
        '''
    bot.sendMessage(chat_id, text)

def giveTodayCoronaState():
    text = f'''
    현재 날짜 {data[0]['date']} 의 코로나 감염 현황 입니다.\n
    확진자 :{data[0]['getCorona']}명 \n
    사망자 :{data[0]['death']}명 \n
    치료중 :{data[0]['care']}명 \n
    검사진행 :{data[0]['exam']}명 \n
    완치자 :{data[0]['clear']}명 \n
    음성결과 :{data[0]['resutlNeg']}명 \n
    누적검사완료 :{data[0]['doneExam']}명 \n
    누적검사 :{data[0]['totalExam']}명 \n
    입니다.\n 감사합니다.
    '''
    bot.sendMessage(chat_id, text)

def giveYesterdayCoronaState():
    text = f'''
    현재 날짜 {data[1]['date']} 의 코로나 감염 현황 입니다.\n
    확진자 :{data[1]['getCorona']}명 \n
    사망자 :{data[1]['death']}명 \n
    치료중 :{data[1]['care']}명 \n
    검사진행 :{data[1]['exam']}명 \n
    완치자 :{data[1]['clear']}명 \n
    음성결과 :{data[1]['resutlNeg']}명 \n
    누적검사완료 :{data[1]['doneExam']}명 \n
    누적검사 :{data[1]['totalExam']}명 \n
    입니다.\n 감사합니다.
    '''
    bot.sendMessage(chat_id, text)
# Keep the program running.
while 1:
    time.sleep(10)