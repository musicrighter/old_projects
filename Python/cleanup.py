"""
   David Gustafson cleanup.py
   CIS 211, Spring 2014

   A program that locates a ditectory, cycles through every file in it,
   and deletes all temporary files.
"""
import sys
import os

def seperate(location):
	for line in os.walk(location):
		top, folder, files = line
		find_files(top, files)

def find_files(top, files):
	temp = ['.aux', '.idx', '.ilg', '.ind', '.log', '.pdf', '.toc']
	for item in files:
		if os.path.splitext(item)[1] in temp:
			print(top + os.path.sep + item)
			os.remove(top + os.path.sep + item)

if __name__ == '__main__':
	seperate(sys.argv[1])