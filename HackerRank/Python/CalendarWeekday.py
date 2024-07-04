# https://www.hackerrank.com/challenges/calendar-module/problem

from calendar import datetime
from calendar import weekday

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
mm, dd, yyyy = map(int, input().split())

# USING DATETIME
# the_date = datetime.datetime(yyyy, mm, dd)
# print(days[the_date.weekday()])

# USING WEEKDAY
the_day = weekday(yyyy, mm, dd)
print(days[the_day])