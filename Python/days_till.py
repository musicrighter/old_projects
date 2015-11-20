"""
days_till.py:  CIS 210 assignment 3, Winter 2014
author: David Gustafson

Figures out number of days between two inputed dates
"""

import sys  # For exit with a message
import argparse # Fancier command line parsing

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

MONTHLEN_leap = [ 0, 31, 29, # February (with leap years)
             31, 30, 31, 30, 31,31, 30, 31, 30, 31, ]

def leap_or_not(year, start_month, start_day, end_month):
    """
    Determines if year is reagular or leap-year. 
    args: year, start_month, start_day, and end_month
    returns: MONTHLEN or MONTHLEN_leap
    effects: result returned
    """
    if start_month > 2:
        year1 = year + 1
    else:
        year1 = year
    if year1 % 4 == 0 and year1 % 100 > 0 and year1 % 400 > 0:
        return MONTHLEN_leap
    elif year1 % 4 == 0 and year1 % 100 == 0 and year1 % 400 == 0:
        return MONTHLEN_leap
    else:
        return MONTHLEN

def is_valid(year, start_month, start_day, end_month, end_day):
    """
    Checks if all inputs are valid. 
    args: year, start_month, start_day, end_month, and end_day 
    returns: prompt or True
    effects: message or result returned
    """
    if year < 1800 or year > 2500:
        return "Must start on a valid date between 1800 and 2500"
    elif start_month < 1 or start_month > 12:
        return "Must start on a valid date between 1800 and 2500"
    elif (start_month == 4 or start_month == 6 or start_month == 9 or start_month == 11) and (start_day < 1 or start_day > 30):
        return "Must start on a valid date between 1800 and 2500"
    elif leap_or_not(year, start_month, start_day, end_month) == MONTHLEN and start_month == 2 and(start_day < 1 or start_day > 28):
        return "Must start on a valid date between 1800 and 2500"
    elif start_day < 1 or start_day > 31:
        return "Must start on a valid date between 1800 and 2500"
    elif end_month < 1 or end_month > 12:
        return "Ending month and day must be part of a valid date"
    elif end_day < 1 or end_day > 31:
        return "Ending month and day must be part of a valid date"
    else:
        return True

def days_in_months(start_month, start_day, end_month, year):
    """
    Figures out number of days in all months. 
    args: start_month, start_day, end_month, and year
    returns: days
    effects: result returned
    """
    days = 0
    leap = leap_or_not(year, start_month, start_day, end_month)
    while start_month != end_month:
        days += leap[start_month]
        start_month += 1
        if start_month == 13:
            start_month = 1
    days += leap_or_not(year, start_month, start_day, end_month)[end_month]
    return days
    
def days_between(start_month, start_day, end_month, end_day, year):
    """
    Figures out the number of days between inputs. 
    args: start_month, start_day, end_month, end_day, and year
    returns: days_between
    effects: result returned
    """
    last_day = leap_or_not(year, start_month, start_day, end_month)[end_month] - end_day
    overcount = start_day + last_day
    all_days = days_in_months(start_month, start_day, end_month, year)
    days_between = all_days - overcount
    return days_between

def main():
    """
    Main program gets year number from command line, 
    invokes computation, reports result on output. 
    args: none (reads from command line)
    returns: none (write to standard output)
    effects: message or result printed on standard output
    """
    ## The standard way to get arguments from the command line, 
    ##    make sure they are the right type, and print help messages
    parser = argparse.ArgumentParser(description="Compute days from yyyy-mm-dd to next mm-dd.")
    parser.add_argument('year', type=int, help="Start year, between 1800 and 2500")
    parser.add_argument('start_month', type=int, help="Starting month, integer 1..12")
    parser.add_argument('start_day', type=int, help="Starting day, integer 1..31")
    parser.add_argument('end_month', type=int, help="Ending month, integer 1..12")
    parser.add_argument('end_day', type=int, help="Ending day, integer 1..31") # 12 to 31
    args = parser.parse_args()  # will get arguments from command line and validate them
    year = args.year
    start_month = args.start_month
    start_day = args.start_day
    end_month = args.end_month
    end_day = args.end_day

    prompt = is_valid(year, start_month, start_day, end_month, end_day)

    if prompt != True:
        sys.exit(prompt)

    if prompt == True:
        print(days_between(start_month, start_day, end_month, end_day, year))

if __name__ == "__main__":
    main()

