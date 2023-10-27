import datetime
from datetime import timedelta
from pytz import timezone

my_date = datetime.datetime.now(timezone('Asia/Kuala_Lumpur'))

timezone_aware = datetime.datetime.now(datetime.timezone(timedelta(hours=8)))

'''
 The first line creates a datetime object representing the current time in the 'Asia/Kuala_Lumpur' timezone, and the second line creates a timezone-aware datetime object representing the current time with a fixed 8-hour offset from UTC.
'''