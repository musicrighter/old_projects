"""
   David Gustafson Card.py
   CIS 211, Spring 2014

   A program that can create either Card or BlackjackCard objects, each are valued 
   differently by points. There are two other functions, one that returns points for 
   a deck, and one that creates a new deck.
"""

class Card:
	'''
	A single playing card
	'''

	syms = {0:'C', 1:'D', 2:'H', 3:'S'}
	cards = {0:'2', 1:'3', 2:'4', 3:'5', 4:'6', 5:'7', 6:'8', 7:'9', 8:'10', 9:'J', 10:'Q', 11:'K', 12:'A'}
	value = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:1, 10:2, 11:3, 12:4}

	def __init__(self, id):
		if id < 0 or id > 51:
			raise ValueError('Card id must be between 0 and 51')
		self._id = id
		self._suit, self._rank = divmod(self._id, 13)   # Seperate id by rank and suit

	def rank(self):
		'''
		Returns rank of card
		'''
		return self._rank

	def suit(self):
		'''
		Returns suit of card
		'''
		return self._suit

	def points(self):
		'''
		Returns points of Card objects
		'''
		return Card.value[self._rank]

	def __repr__(self):
		return str(Card.cards[self._rank]) + Card.syms[self._suit]

	def __lt__(self, other):
		return self._id < other._id
		

class BlackjackCard(Card):
	'''
	A single playing card
	'''

	value = {0:2, 1:3, 2:4, 3:5, 4:6, 5:7, 6:8, 7:9, 8:10, 9:10, 10:10, 11:10, 12:11}

	def __init__(self, id):
		super().__init__(id)

	def points(self):
		'''
		Returns points of BlackjackCard objects
		'''
		return BlackjackCard.value[self._rank]
	
	def __lt__(self, other):
		return self._rank < other._rank

def points(deck):
	'''
	Returns combined points for inputted list of Card or BlackjackCard objects
	Args:
		deck: a list of Card or BlackjackCard objects
	Returns:
		sum of cards in list
	'''
	return sum(card.points() for card in deck)

def new_deck(cls=Card):
	'''
	Creates a deck of Card or BlackjackCard objects
	Args:
		Nothing or kind: the type of deck to make
	Returns:
		cards: the list of 52 Card or BlackjackCard objects
	'''
	return [cls(i) for i in range(52)]