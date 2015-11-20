"""
   David Gustafson backup.py
   CIS 211, Spring 2014

   A program that will create a directory named version (if there isn't one)
   and then backup the inputted location as a new file in version.
   Everytime it is called afterwards, it will backup another new file.
"""
import sys
import os
from shutil import copytree

def create_dir(name):
	if os.path.isdir(name) == False:
		os.mkdir(name)

def back_up(location, name):
	counter = 1
	for folder in os.listdir(name):
		counter += 1
	copytree(location, name + os.path.sep + str(counter))

if __name__ == '__main__':
	create_dir('version')
	back_up(sys.argv[1], 'version')