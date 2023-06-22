from datetime import datetime as dt
from datetime import date, time
import pytz

current_date_time = dt.now()

print("Get today's date")
current_date = date.today()
print(current_date)

print("--Date Object--")
d = date(2019, 4, 13)
print(d)

print("--date from a timestamp--")
timestamp = date.fromtimestamp(1326244364)
print("Date=", timestamp)

# date object of today's date
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

a=time()
print("a=",a)

print(current_date_time.date())
print(current_date_time.time())

b=time(11,34,56)
print("b=",b)

c=time(hour=11,minute=34,second=56)
print("c=",c)

d = time(11,34,56,234566)
print("d=",d)

print("-display hour,minute,second,microsecond-")

# A timedelta object represents difference between two dates or times
t1 = date(year=2018, month=7, day=12)
t2 = date(year=2017, month=12, day=23)

t3 = t1-t2
print("t3=", t3)

print("--using timedelta objects--")
from datetime import timedelta

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2
print("t3=", t3)

t4 = dt(year=2018, month=7, day=12, hour=7, minute=9, second=33)
t5 = dt(year=2019, month=6, day=10, hour=5, minute=55, second=13)
t6 = t5 - t4
print("t6 days", t6.days)
print("t6 seconds", t6.seconds)
print("t6=", t6.seconds)
print(type(t6))

# format date using strftime()
now = dt.now()
t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y,%H:%M:%S")
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y,%H:%M:%S")
print("s2:", s2)
print(type(s2))

# converting string to date time
date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = dt.strptime(date_string, "%d %B, %Y")
print("date_object=", date_object)

local = dt.now()
print("Local:",local.strftime("%m/%d/%y,%H:%M:%S"))

tz_NY = pytz.timezone('America/New_York')
datetime_NY = dt.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = dt.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

# yielding a set of dates within date range.
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


start_date = date(2013, 1, 1)
end_date = date(2015, 6, 2)
for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))







