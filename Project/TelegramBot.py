import time
import telepot
from CoronaStateXMLParsing import data

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
    elif "뭐해" in msg['text']:
        bot.sendMessage(chat_id, "명령을 기다리고 있어요!")
    elif ("금일"in msg['text'] or "오늘" in msg['text']) and ("감염"in msg['text'] or "확진자" in msg['text']):
        giveTodayCoronaState()
        
    elif ("전일" in msg['text'] or "어제" in msg['text']) and ("감염"in msg['text'] or "확진자" in msg['text']):
        giveYesterdayCoronaState()
    else:
        bot.sendMessage(chat_id, "다시한번말해주세요 이해를 못했어요!")

bot.message_loop(handle)


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