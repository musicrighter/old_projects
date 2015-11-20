import sys

MONTHS = ['x','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
DAYS_IN_MONTH = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def days_ahead(start_month, start_day, ahead):
	total_ahead = start_day + ahead
	month = start_month
	while total_ahead > DAYS_IN_MONTH[month]:
		total_ahead = total_ahead - DAYS_IN_MONTH[month]
		if month == 12:
			month = 1
		else:
			month += 1
	return MONTHS[month] + ' ' + str(total_ahead)

start_month = int(sys.argv[1])
start_day = int(sys.argv[2])
ahead = int(sys.argv[3])

print(days_ahead(start_month, start_day, ahead))

# print(days_ahead(3, 14, 45))   # My birthday from today