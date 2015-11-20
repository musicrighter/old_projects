"""
   David Gustafson Deck.py
   CIS 211, Spring 2014

   A program that can create a list of either Deck or PinochleDeck objects. One of these objects
   is a deck of Card objects, 52 for Deck and 48 for PinochleDeck. Objects can be shuffled, 
   dealt, restored, sorted, and any other built-in funtions for a list provided by python.
"""

from Card import *
import random

class Deck(list):
	'''
	A deck of 52 Card objects
	'''

	def __init__(self):
		# for i in range(52):
		# 	self.append(Card(i))

		[self.append(Card(i)) for i in range(52)]

	def shuffle(self):
		'''
		Returns shuffled deck
		'''
		return random.shuffle(self)

	def deal(self, n):
		'''
		Removes an inputted number of cards from a deck
		Returns these cards as a new list
		'''
		return [self.pop(0) for i in range(n)]

	def restore(self, a):
		'''
		Appends a list of cards to a deck
		'''
		for card in a:
			if type(card) != Card:
				raise ValueError('Decks may only contain Card objects')
			self.append(card)
		return 

class PinochleDeck(Deck):
	'''
	A deck of 48 Card objects
	'''

	pin_deck = [7,8,9,10,11,12]

	def __init__(self):
		for i in range(52):
			if Card(i).rank() in PinochleDeck.pin_deck:
				self.append(Card(i))
				self.append(Card(i))
