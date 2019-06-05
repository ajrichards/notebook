#!/usr/bin/env python

"""
date – Manipulate just date ( Month, day, year)
time – Time independent of the day (Hour, minute, second, microsecond)
datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
timedelta— A duration of time used for manipulating dates
tzinfo— An abstract class for dealing with time zones
"""

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

## working with just the date
today = date.today()

print("----------------------------")
print("today is {}".format(today))
print("today is {} {} {}".format(today.month, today.day, today.year))
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("today's weekday is {}".format(days[today.weekday()]))


## working with date and time
print("----------------------------")
today = datetime.now()
print("today is {}".format(today))
print("today is {} {} {}".format(today.month, today.day, today.year))
print("time from datetime",datetime.time(today))

## string formatting
print("----------------------------")
today = datetime.now()
print("year:", today.strftime("%Y"))
print("year:", today.strftime("%y"))
print("month:", today.strftime("%B"))
print("day:", today.strftime("%d"))
print("weekday:", today.strftime("%a"))
print("date:", today.strftime("%x"))
print("time:", today.strftime("%X"))


## Timedelta Objects
print("----------------------------")
print("one year from now it will be: ", str(today + timedelta(days=365)))
print("40 days from now it will be: ", str(today + timedelta(days=40)))
print("10 weeks and 2 days...",str(today + timedelta(weeks=10,days=2)))

my_birthday = datetime(today.year,11,23)

if my_birthday < today:
    print("birthday has passed ({} days ago)".format((today-my_birthday).days))
else:
    print("birthday still to come ({} days from now)".format((my_birthday-today).days))

## get last Monday
def get_last_monday():
    today = datetime.now()

    for days_ago in range(7):
        day = today - timedelta(days=days_ago)
              
        if day.strftime("%A") == 'Monday':
            return(day)

print(today.strftime("%A"))
last_monday = get_last_monday()
print(last_monday)

    
