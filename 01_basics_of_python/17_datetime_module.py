import datetime

# create custom dates
my_date = datetime.date(2003, 7, 23)
print(my_date)

# get todays date
today_date = datetime.date.today()
print(today_date)
print("year :", today_date.year)
print("month :", today_date.month)
print("day :", today_date.day)
print('weekday :', today_date.weekday()) # monday - 0 & sunday - 6
print("isoweekday :", today_date.isoweekday()) # monday - 1 & sunday - 7

delta = datetime.timedelta(days=7)
print(today_date - delta)
print(today_date + delta)

bday = datetime.date(2023, 7, 23)
till_bday = bday - today_date
print(till_bday)
print(till_bday.days)

t = datetime.time(9, 54, 22, 0)
print(t)
print(t.hour)

t = datetime.datetime.now()
print(t)
print(t + delta)

import pytz

dt = datetime.datetime.now(tz=pytz.UTC)
print(dt)