from tkinter import *
import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase
import ShoppingList as SL
def writeyourEmail():
    miniwindow = Tk()
    miniwindow.title("Email")
    miniwindow.geometry("400x200+500+500")
    miniwindow.configure(background='powderblue')
    miniwindow.resizable(0, 0)  # 창 크기 고정
    info = Label(miniwindow, text='전송받으실 이메일 주소를 입력하세요.',font=('서울서체', 15, 'bold'), bg = 'powderblue')
    info.place(x=30,y=50)
    global getEmail
    getEmail = Entry(miniwindow)
    getEmail.place(x=40,y=100,height=25)
    getEmail.configure( width=45, bg= 'white',font=('서울서체', 10, 'bold'))
    btnSearch = Button(miniwindow, text="전송", width=10, command =lambda: sendingEmail())
    btnSearch.place(x=300, y=150, height=30)
    btnSearch.configure(background='white', font=('서울서체', 10, 'bold'))

def sendingEmail():
    me = 'dnk97@naver.com'
    you = getEmail.get()

    msg = MIMEMultipart()
    msg['Subject'] = '코로나종합상황센터 방역쇼핑몰에서 전송된 메일입니다.'
    msg['From'] = me
    msg['To'] = you



    html = MIMEText(
                    '''<html>

                                <head></head>
                                <body>
                                    선택하신상품의 정보입니다.<br><br>
                                    상품명 : '''+(SL.product_title)+'''<br>
                                    상품가격 : '''+(SL.product_price)+'''<br>
                                    <img src='''+(SL.proudct_imageURL)+'''><br>
                                    상품사이트로 이동하시려면 하단의 링크를 클릭하여주세요!<br>
                                    상품판매처 -><a href='''+(SL.product_URL)+'''>ClickHere!!</a><br>
                                    감사합니다.<br>
                                </body>
                            </html>''','html')



    msg.attach(html)
    # 네이버 버전
    naver_server = smtplib.SMTP_SSL('smtp.naver.com', 465)
    naver_server.login("dnk97@naver.com", "81ZYNUBWGKDH")
    naver_server.sendmail(me, [you], msg.as_string())
    naver_server.quit()
    print("Email Sending Complete!!")

#구글 버전
# google_server = smtplib.SMTP_SSL('smtp.google.com', 465)
# google_server.login('dnk972001@gmail.com', 'dn97119738')
# google_server.sendmail(me, [you], msg.as_string())
# google_server.quit()

