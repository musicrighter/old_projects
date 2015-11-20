"""
calpr.py:  CIS 210 assignment 2a, Winter 2014
author: David Gustafson

print a calendar that matches the month and year inputed
"""

import sys 
import datetime  

USAGE = """
Usage: calpr.py 12 2014
  where 12 can be replaced by any month 1..12
  and 2014 can be replaced by any year 1..2100
"""

if len(sys.argv) != 3:
	print(USAGE)
	exit(1)
	       
month = int(sys.argv[1])
year = int(sys.argv[2])

MONTHLEN = [ 0, # No month zero
	31, # 1. January
	28, # 2. February (ignoring leap years)
	31, # 3. March
	30, # 4. April
	31, # 5. May
	30, # 6. June
	31, # 7. July
	31, # 8. August
	30, # 9. September
	31, #10. October
	30, #11. November
	31, #12. December
	]

# What day of the week does year,month begin on? 
a_date = datetime.date(year, month, 1)
starts_weekday = a_date.weekday()
## a_date.weekday() gives 0=Monday, 1=Tuesday, etc.
## Roll to start week on Sunday
starts_weekday = (1 + starts_weekday) % 7  


month_day = 1   
last_day = MONTHLEN[month]  

print(" Su Mo Tu We Th Fr Sa")

# First week
for i in range(7):
	if i < starts_weekday :
		print("   ", end="")
	else:
		print(format(month_day, "3d"), end="")
		month_day += 1
print()

# Whole weeks
for i in range(21):
    print(format(month_day, "3d"), end="")
    month_day += 1
    if i == 6:
        print()
    if i == 13:
        print()
print()

# Last week (and possibly a day or two extra)
for i in range(15):
    print(format(month_day, "3d"), end="")
    if month_day == last_day:
        break
    if i == 6:
        print()
    month_day += 1
