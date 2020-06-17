import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase
import ShoppingList as SL
def writeyourEmail():
    miniwindow = Tk()
def sendingEmail():
    me = 'dnk97@naver.com'
    you = 'dnk972001@kpu.ac.kr'

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

