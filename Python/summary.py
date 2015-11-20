"""
   David Gustafson summary.py
   CIS 211, Spring 2014

   A program that alloys someone to display a customers video renting info. It shows late fees and calculates the monthly cost as well.
"""
from sqlite3 import *
import sys
from datetime import datetime


def get_name():
	'''
	displays a message that includes customers first and last names
	'''
	cur.execute('select first_name, last_name from customer where last_name = ?', (name.upper(),))

	[(first,last)] = cur.fetchall()
	names = str(first.capitalize()) + ' ' + str(last.capitalize())

	print('\n--- Sakila DVD Rentals ---\n\nMonthly report for {}\n'.format(names))


def get_info():
	'''
	displays the customers movie renting info including title, rental_duration, late fees and total monthly cost.
	'''
	cur.execute('''select title, rental_date, rental_duration, return_date, rental_rate from customer join rental using (customer_id) 
	join inventory using (inventory_id) join film using (film_id) where last_name = ?''', (name.upper(),))

	inform = cur.fetchall()

	date_format = "%Y-%m-%d %H:%M:%S.%f" 
	total = 0

	for line in inform:
		title, rental_date, rental_duration, return_date, rental_rate = line[0:]
		title = title.title()
		rented = datetime.strptime(rental_date, date_format)
		returned = datetime.strptime(return_date, date_format)
		diff = returned - rented
		new_date = str(Date.month) + '/' + str(Date.day) + '/' + str(Date.year)
		if rented.month == int(month) and rented.year == int(year):
			money = '  $' + str(rental_rate)
			if diff.days > rental_duration:
				print(title.ljust(25),rented.date(), money)
				total += rental_rate
				print('**late fee'.rjust(25), returned.date(), money)
				total += rental_rate
			else:
				print(title.ljust(25),rented.date(), money)
				total += rental_rate

	print('\nMonthly total:', '$' + str(format(total, '10,.2f')))


if __name__ == '__main__':
	name = sys.argv[1]
	year = sys.argv[2]
	month = sys.argv[3]

	db = connect('sakila.db')
	cur = db.cursor()

	get_name()
	get_info()
