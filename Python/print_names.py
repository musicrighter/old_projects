"""
print_names.py: CIS 211 assignment 1b, Spring 2014
authors: David Gustafson

A program that will read a set of names from a text ﬁle and 
print them in the terminal window in the order specified.
"""

import sys 

if len(sys.argv) < 3:
	raise ValueError('Please enter the program filename, text filename, and sorting order (and "inits")')
name_file = sys.argv[1]
order = sys.argv[2].lower()
if len(sys.argv) == 4:
	inits = sys.argv[3].lower()
else:
	inits = ''

class Name:
	'''
	A single name, both first and last
	'''
	def __init__(self, first_name='', last_name=''):
		'''
		Seperates out first name and last name
		'''
		self._first = first_name
		self._last = last_name

	def __lt__(self, other):
		if self.last() < other.last():
			return True
		elif self.last() == other.last():
			return self.first() < other.first()
		else:
			return False

	def first(self):
		'''
		Returns first name
		'''
		return self._first

	def last(self):
		'''
		Returns last name
		'''
		return self._last

def name_list(file_name):
	'''
	Creates a list of objects for all names in a text file
	Args:
		file_name: The text file that contains names
	Returns:
		names: List of name objects, first and last
	'''
	names = []
	with open(file_name, 'r') as my_file:
		for line in my_file:
			line = line.split()
			name = Name(line[0], line[1])
			names.append(name)
	return names

def print_names(file_name, order):
	'''
	Prints names in order specified
	Args:
		file_name: The text file that contains names
		order: The order the names will be sorted
	Effects:
		Prints names
	Returns:
		Nothing
	'''
	a = name_list(file_name)
	if order == 'first':
		a.sort(key = Name.first)
		if inits == 'inits':
			for name in a:
				print(name.first()[0] + '.', name.last())
		else:
			for name in a:
				print(name.first(), name.last())
	elif order == 'last':
		a.sort()
		if inits == 'inits':
			for name in a:
				print(name.last() + ',', name.first()[0] + '.')
		else:
			for name in a:
				print(name.last() + ',', name.first())

if __name__ == '__main__':
	print_names(name_file, order)