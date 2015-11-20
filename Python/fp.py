"""
   David Gustafson fp.py
   CIS 211, Spring 2014

   A group of funtions and a class that do various things, such as splitting
   strings and returning only vowels or only digits, and getting the area
   of a house room by room.
"""
from string import punctuation

def codes(string):
	return list(map(ord, string))

def vowels(string):
	return ''.join(filter(lambda ch: ch in 'aeiouAEIOU', list(string)))

def tokens(string):
	return list(map(lambda x: x.strip(punctuation), string.split()))

def numbers(string):
	return list(filter(lambda x: x.isdigit(), tokens(string)))

def sq_ft(file_name):
	return sum(map(lambda line: Room(line).area(), open(file_name)))

class Room:
	def __init__(self, info):
		self._info = info
		self._name, self._width, self._depth = list(self._info.split())[0:]
	def area(self):
		return float(self._width) * float(self._depth)

# def checksum(stringfrom ):
# 	s = stringfrom 
# 	return ':'.join(hex(ord(x))[2:] for x in s)
