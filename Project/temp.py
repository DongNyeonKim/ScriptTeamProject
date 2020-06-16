from datetime import datetime, timedelta

today = datetime.now()
todayDate = today.strftime("20%y%m%d")
b7Date = today + timedelta(days=-8)
b8Date = b7Date.strftime("20%y%m%d")

print(todayDate)
print(b8Date)