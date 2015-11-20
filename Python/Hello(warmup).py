"""
hello.py: CIS 211 assignment 1a, Spring 2014
authors: David Gustafson

A program that will print a “hello, world” message in any available inputted language.
If there is nothing else on the command line besides the name of the program, or the 
language isn't available, the greeting will be printed in English
"""

import sys

if len(sys.argv) != 2:
	raise ValueError('Please enter the program filename or both the program and a language')

if (len(sys.argv) = 1):
	lang = 'english'
else:
	lang = str(sys.argv[1])
	lang = lang.lower()


def hello(lang):
	'''
	Returns the greeting for an inputted language
	Args:
		lang: a language 
	Returns:
		greeting: the greeting "Hello, world" in inputted language
	'''
	greeting = options[lang]
	return greeting


options = {'english':'Hello, world', 'french':'Bonjour tout le monde', 'spanish':'Hola mundo', 
		   'german':'Hallo Welt', 'italian':'Ciao mondo', 'russian':'Privet mir'}

if __name__ == '__main__':
	if lang in options:     # Making sure the language is available
		print(hello(lang))
	else:
		print("Sorry, I don't speak", lang.capitalize())