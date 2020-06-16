import smtplib
from email.mime.text import MIMEText

me = 'dnk97@naver.com'
you = 'dnk972001@kpu.ac.kr'
contents = '안녕하세요'

msg = MIMEText(contents, _charset='euc-kr')
msg['Subject'] = '코로나종합상황센터에서 전송된 메일입니다.'
msg['From'] = me
msg['To'] = you

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

