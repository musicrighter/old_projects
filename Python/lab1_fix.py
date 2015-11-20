import random 

class MyError(Exception):
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)


class Animal:
	def __init__ (self, id):
		""" 
		our animals are represented by id, the mapping is like below:
		1 : 'fly',
		2 : 'dragonfly',
		3 : 'frog',
		4 : 'fox',
		5 : 'wolf',
		6 : 'tiger'
		Instead of string representations, we just use id number to save storage.
		In short, the constructor takes an id number and assigns it to an instance variable
		Do NOT change anything in this constructor
		"""

		if id > 0 and id < 7:
			self.id = id
		else:
			raise MyError("invalid id, a valid id should range between 1 to 6")
		
	'''try to use dictionary in the following functions'''
	
	'''define a function named name() which returns the name (frog, fly, tiger...) of the animal'''
	def name(self):
		
	'''define a function named type() which returns the type (mammal, insect...)'''
	def type(self):
		
	
	def __repr__(self):
		"""
		This function should 'translate' the animal from id number to string representation
		The representation is dynamically determined according to id.
		Not only the animal's names, but also you should add its type. 
		The mapping is like below:
		1 : 'fly insect',
		2 : 'dragonfly insect',
		3 : 'frog amphibian',
		4 : 'fox mammal',
		5 : 'wolf mammal',
		6 : 'tiger mammal'
		tips: if and elif statements are cumbersome, use dictionary.
		If you have finished the name() and type() function this one won't be that hard
		"""

		
def main():
	
	#this is for testing purposes, correct outputs should be :
	#tiger 
	#mammal
	#dragonfly
	#insect
	#tiger mammal
	#dragonfly insect
	tiger = Animal(6)
	dragonfly = Animal(2)
	print(tiger.name())
	print(tiger.type())
	print(dragonfly.name())
	print(dragonfly.type())
	
	#test __repr__
	print(tiger)
	print(dragonfly)
	

if __name__ == "__main__":
    main()
	
