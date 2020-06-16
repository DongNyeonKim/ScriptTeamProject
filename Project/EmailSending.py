import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase

me = 'dnk97@naver.com'
you = 'dnk972001@kpu.ac.kr'
contents = '안녕하세요'

msg = MIMEMultipart()
msg['Subject'] = '코로나종합상황센터에서 전송된 메일입니다.'
msg['From'] = me
msg['To'] = you



html = MIMEText(
                '''<html>
                            <head></head>
                            <body>
                                Hi ${NAME}.<br>
                                <img src="https://shopping-phinf.pstatic.net/main_8238249/82382493518.2.jpg?type=f200"><br>
                                This is a test message.
                            </body>
                        </html>''','html')



msg.attach(html)
print(html)

# 네이버 버전
naver_server = smtplib.SMTP_SSL('smtp.naver.com', 465)
naver_server.login("dnk97@naver.com", "81ZYNUBWGKDH")
naver_server.sendmail(me, [you], msg.as_string())
naver_server.quit()

#구글 버전
# google_server = smtplib.SMTP_SSL('smtp.google.com', 465)
# google_server.login('dnk972001@gmail.com', 'dn97119738')
# google_server.sendmail(me, [you], msg.as_string())
# google_server.quit()

