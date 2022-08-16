import datetime

# create custom dates
my_date = datetime.date(2003, 7, 23)
print(my_date)

# get todays date
today = datetime.date.today()
print(today)
print("year :", today.year)
print("month :", today.month)
print("day :", today.day)
print('weekday :', today.weekday()) # monday - 0 & sunday - 6
print("isoweekday :", today.isoweekday()) # monday - 1 & sunday - 7