import time
import telepot

token = "1285432386:AAF_04K0iMDFYSMFf9v8r0rUUzfEpR4Ptl0"
bot = telepot.Bot(token)
chat_id ="1273211346"

def sendStartMessage():
    bot.sendMessage(chat_id, "코로나 종합상황센터 텔레그램 챗봇을 시작합니다!")