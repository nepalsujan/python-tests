# from datetime import datetime
# import time

# print ("datetime.now(): ",datetime.now())
# # /home/sujan/Desktop/MoneyHoney/Associate/mmp-b-ws/apps/testdate.py
# print ("datetime.now(): ",datetime.now().date())

# today = time.strftime("%d/%m/%Y")
# print (today)

# today_format = datetime.strptime(today, "%m/%d/%Y")
# print (today_format)

# if today > "13/07/2023":
#     print ("true")
# else:
#     print ("true no")

# if "2023-07-15T03:04:15.085Z" > today:
#     print (True)
import pytz
from datetime import datetime
tz = pytz.timezone('Asia/Kuala_Lumpur')
#from end user
a = datetime(2023, 7, 10)
time_aware= tz.localize(a)
time_aware= tz.localize(a).date()
print (time_aware)
print (datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).date())

#comaprision in malaysian time
if time_aware >= datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).date():
    if time_aware == datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).date():
        print ("needed same time ")
    else: 
        print ("much beteter ")
else : 
    print("invalid")

