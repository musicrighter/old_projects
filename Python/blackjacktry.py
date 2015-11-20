"""
   David Gustafson blackjack.py
   CIS 211, Spring 2014

   A program that allows a user to play blackjack. The standard rules apply and there can be up to 6 cards.
   Counters for dealers wins and score along with players wins and score. 
"""
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from random import randint
import random
from CardLabel import *
from Card import *
from prompt import everything

def total(hand):
	'''
	Returns sum of points for a hand of cards.
	'''
	result = 0
	numAces = 0

	for card in hand:
		result += card.points()
		if card.rank() == 12:
			numAces += 1

	while result > 21 and numAces > 0:
		result -= 10
		numAces -= 1

	return result

hand = []
dealer_hand = []

def new_deal():
	'''
	Deals a new hand of blackjack cards, 2 face up for the player,
	1 face down and 1 face up for the dealer
	'''

	available()

	num = 0
	count = 0
	hand = []
	dealer_hand = [] 

	deck = new_deck(BlackjackCard)
	random.shuffle(deck)
	unavailable(False)

	dealer_card = deck.pop()

	onetop.display('back', dealer_card._id)
	dealer_two = deck.pop()
	dealer_hand.append(dealer_two)
	twotop.display('front', dealer_two._id)
	threetop.display('blank')
	fourtop.display('blank')
	fivetop.display('blank')
	sixtop.display('blank')

	one_card = deck.pop()
	hand.append(one_card)
	one.display('front', one_card._id)
	two_card = deck.pop()
	hand.append(two_card)
	two.display('front', two_card._id)
	three.display('blank')
	four.display('blank')
	five.display('blank')
	six.display('blank')

	configure(seventop)
	configure(seven)

	if total(hand) == 21 and len(hand) == 2:
		showinfo('You Win!', 'Blackjack!')
		player_wins += 1
		configure(seventop)
		configure(seven)
		balance += int(bet*1.5)
		bet = int(bet*1.5)
		configure(twelve)
		ten.configure(text='Balance: ' + str(balance), font=('Helvetica', '16'))
		Bet['state'] = 'normal'
		unavailable()
		# new_deal()
	twelve.configure(text='Game winnings: 0', font=('Helvetica', '12'))

num = 0	
dealer_wins = 0
player_wins = 0
# balance = 0

def hit_card():
	'''
	Deals a new card to be added to the players hand, can be done until sum of hand
	is over 21.
	'''
	global deck, num, hand, dealer_wins, bet, balance

	counter = [three, four, five, six]	
	next_card = deck.pop()
	hand.append(next_card)
	counter[num].display('front', next_card._id)
	num += 1

	configure(seventop)
	Double['state'] = 'disabled'

	if total(hand) > 21:
		showinfo('Game over', 'You bust, Dealer wins...')
		dealer_wins += 1
		configure(seven)
		configure(twelve, True)
		balance -= bet
		configure(ten)
		Bet['state'] = 'normal'
		unavailable()
		# new_deal()
		update()

count = 0

def pass_card(double=False):
	'''
	Flips over the dealers card and totals up points for each hand, determines who wins.
	'''
	global dealer_card, dealer_hand, count, player_wins, dealer_wins, bet, balance, new_bet

	onetop.display('front', dealer_card._id)
	dealer_hand.append(dealer_card)

	counter = [threetop, fourtop, fivetop, sixtop]

	configure(seventop)

	while total(dealer_hand) < 17:
		next_card = deck.pop()
		dealer_hand.append(next_card)
		counter[count].display('front', next_card._id)
		count += 1
		configure(seventop)

	dealer = total(dealer_hand)
	player = total(hand)

	if dealer > 21 and player <= 21:
		showinfo('Game over', 'Dealer bust, You Win!')
		player_wins += 1
		configure(seven)
		if double == True:
			balance += new_bet * 1.5
		else:
			balance += bet
		configure(twelve)	
		configure(ten)
		Bet['state'] = 'normal'
		unavailable()
	elif dealer == player:
		showinfo('Game over', 'Push, Tie game...')
		Bet['state'] = 'normal'
		unavailable()
	elif dealer <= 21 and dealer > player:
		showinfo('Game over', 'So close, Dealer wins...')
		dealer_wins += 1
		configure(seven)
		if double == True:
			balance -= new_bet 
		else:
			balance -= bet
		configure(twelve, True)
		configure(ten)
		Bet['state'] = 'normal'
		unavailable()
	else:
		showinfo('Game over', 'You Win!')
		player_wins += 1
		configure(seven)
		if double == True:
			balance += new_bet * 1.5
		else:
			balance += bet
		configure(twelve)
		configure(ten)
		Bet['state'] = 'normal'
		unavailable()
	# new_deal()
	if double == True:
		thirteen.config(text='Bet: ' + str(bet))
	update()

def double():
	global bet, deck, hand, new_bet
	new_bet = int(bet)*2
	thirteen.config(text='Bet: ' + str(new_bet))
	one_card = deck.pop()
	three.display('front', one_card._id)
	hand.append(one_card)
	pass_card(double=True)


def quit_it():
	res = askquestion('Quit Game', 'Do you want to stop this game?')
	if res == 'yes':
		update()
		quit()

def key_handler(event):
	'''
	Handles the keypress entry and calls the appropriate functions.
	'''
	if event.keysym == 'q':
		Hit.invoke()
	elif event.keysym == 'w':
		Pass.invoke()
	elif event.keysym == 'e':
		Deal.invoke()
	elif event.keysym == 'r':
		Buyin_entry.invoke()
	elif event.keysym == 't':
		Double.invoke()
	elif event.keysym == 'y':
		res = askquestion('Quit Game', 'Do you want to stop this game?')
		if res == 'yes':
			update()
			quit()

def buyin_submit():
	'''
	Displays inputted accoount balance.
	'''
	global balance
	balance = int(Amount.get())
	configure(ten)
	Amount['state'] = 'readonly'

def bet_submit():
	'''
	Raises messages if entry are incorrect.
	'''
	global bet, balance
	bet = int(Bet.get())
	available()
	Bet['state'] = 'readonly'

def available():
	global bet, balance
	if balance <= 0:
		showinfo('Out of money?', "Please enter a buy-in or quit the game")
		Deal['state'] = 'disabled'
		Hit['state'] = 'disabled'
		Pass['state'] = 'disabled'
		Double['state'] = 'disabled'

	if bet > balance:
		showinfo('Out of money?', "Can't bet more than you have!")
		bet = balance
	thirteen.config(text='Bet: ' + str(bet))

def unavailable(opp=True):
	if opp == True:
		Hit['state'] = 'disabled'
		Pass['state'] = 'disabled'
		Double['state'] = 'disabled'
	else:
		Hit['state'] = 'normal'
		Pass['state'] = 'normal'
		Double['state'] = 'normal'

def configure(option, minus=False, bet=True):
	if bet == False:
		bet = new_bet
	if option == seven:
		seven.configure(text='Dealer wins: ' + str(dealer_wins) + '\n\nYour wins: ' + str(player_wins), font=('Helvetica', '10'))
	elif option == seventop:
		seventop.configure(text='Dealer score: ' + str(total(dealer_hand)) + '\n\nYour score: ' + str(total(hand)), font=('Helvetica', '14'))
	elif option == ten:
		ten.configure(text='Balance: ' + str(balance), font=('Helvetica', '16'))
	elif option == twelve:
		if minus == False:
			twelve.configure(text='Game winnings: ' + str(bet), font=('Helvetica', '12'))
		else:
			twelve.configure(text='Game winnings: ' + str(-bet), font=('Helvetica', '12'))

def update():
	global name, dealer_wins, player_wins, balance
	count = 0
	with open('people.txt', 'r') as my_file:
		data = my_file.readlines()
		for line in data:
			line = (line.strip()).split()
			person, dealer, player, amount, password = line
			if name == person:
				dealer = dealer_wins
				player = player_wins
				amount = balance
				data[count] = str(name) + ' ' + str(dealer_wins) + ' ' + str(player_wins) + ' ' + str(balance) + ' ' + str(password) + '\n'

				with open('people.txt', 'w') as last_file:
					last_file.writelines(data)
				return
			count += 1


name, dealer_wins, player_wins, balance, password, good = everything()
if good == False:
	quit()
dealer_wins = int(dealer_wins)
player_wins = int(player_wins)
balance = int(balance)
	
root = tk.Tk()
root.configure(bg='deep sky blue')
root.geometry("790x440")
greeting = 'Welcome back ' + str(name)
greeting1 = 'Welcome', name
if (name != 'None') and (dealer_wins or player_wins > 0):
	root.title(greeting)
elif name != 'None':
	root.title(greeting1)
else:
	root.title('Welcome')

CardLabel.load_images()
panel = tk.Label(root, image = CardLabel.bjimg)
panel.grid(row=0, column=0, rowspan=8, columnspan=8)


root.bind_all('<Key>', key_handler) 

bet = 0

for row in range(2):
	root.rowconfigure(row, minsize=130)
for col in range(6):
	root.columnconfigure(col, minsize=100)
root.columnconfigure(6, minsize=180)

# account balance enrty

Amount = tk.Entry(root)
Amount.grid(row=4, column=0, columnspan=2)

Bet = tk.Entry(root)
Bet.grid(row=4, column=2, columnspan=2)

# top row labels

onetop = CardLabel(root)
onetop.grid(row=0, column=0, padx = 10, pady = 10)

twotop = CardLabel(root)
twotop.grid(row=0, column=1, padx = 10, pady = 10)

threetop = CardLabel(root)
threetop.grid(row=0, column=2, padx = 10, pady = 10)

fourtop = CardLabel(root)
fourtop.grid(row=0, column=3, padx = 10, pady = 10)

fivetop = CardLabel(root)
fivetop.grid(row=0, column=4, padx = 10, pady = 10)

sixtop = CardLabel(root)
sixtop.grid(row=0, column=5, padx = 10, pady = 10)

seventop = tk.Label(root, text='Dealer score: 0\n\n Your score: 0', font=('Helvetica', '14'))
seventop.grid(row=1, column=6, padx = 10, pady = 10)
seventop['bg'] = 'light blue'

# bottom row labels

one = CardLabel(root)
one.grid(row=1, column=0, padx = 10, pady = 10)

two = CardLabel(root)
two.grid(row=1, column=1, padx = 10, pady = 10)

three = CardLabel(root)
three.grid(row=1, column=2, padx = 10, pady = 10)

four = CardLabel(root)
four.grid(row=1, column=3, padx = 10, pady = 10)

five = CardLabel(root)
five.grid(row=1, column=4, padx = 10, pady = 10)

six = CardLabel(root)
six.grid(row=1, column=5, padx = 10, pady = 10)

seven = tk.Label(root, text='Dealer wins: ' + str(dealer_wins) + '\n\nYour wins: ' + str(player_wins), font=('Helvetica', '10'))
seven.grid(row=0, column=6, padx = 10, pady = 10)
seven['bg'] = 'light blue'

nine = tk.Label(root, text='Initial buy-in:', font=('Helvetica', '10'))
nine.grid(row=3, column=0, columnspan=2, padx = 10, pady = 10)
nine.config(bg='deep sky blue')

ten = tk.Label(root, text='Balance: ' + str(balance), font=('Helvetica', '16'))
ten.grid(row=2, column=4, columnspan=3, padx = 10, pady = 10)
ten.config(bg='deep sky blue')

eleven = tk.Label(root, text='Bet:', font=('Helvetica', '10'))
eleven.grid(row=3, column=2, columnspan=2, padx = 10, pady = 10)
eleven.config(bg='deep sky blue')

twelve = tk.Label(root, text='Game winnings: 0', font=('Helvetica', '12'))
twelve.grid(row=3, column=4, columnspan=3, padx = 10, pady = 10) 
twelve.config(bg='deep sky blue')

thirteen = tk.Label(root, text='Bet: 0', font=('Helvetica', '12'))
thirteen.grid(row=4, column=4, columnspan=3, padx = 10, pady = 10) 
thirteen.config(bg='deep sky blue')

# buttons

Deal = tk.Button(root, text='Deal', font=('Helvetica', '12', 'bold'), command=new_deal) 
Deal.grid(row=2, column=0, pady = 10)
Deal['bg'] = 'light blue'
Deal['width'] = 5

Hit = tk.Button(root, text='Hit', font=('Helvetica', '12', 'bold'), command=hit_card) 
Hit.grid(row=2, column=1, pady = 10)
Hit['bg'] = 'light blue'
Hit['width'] = 5

Pass = tk.Button(root, text='Hold', font=('Helvetica', '12', 'bold'), command=pass_card) 
Pass.grid(row=2, column=2, pady = 10)
Pass['bg'] = 'light blue'
Pass['width'] = 5

Double = tk.Button(root, text='Double', font=('Helvetica', '12', 'bold'), command=double)
Double.grid(row=2, column=3, pady = 10)
Double['bg'] = 'light blue'
Double['width'] = 5

Quit = tk.Button(root, text='Quit', font=('Helvetica', '12', 'bold'), command=quit_it)
Quit.grid(row=2, column=4, pady = 10)
Quit['bg'] = 'light blue'
Quit['width'] = 5

Buyin_entry = tk.Button(root, text='Submit buy-in', font=('Helvetica', '10'), command=buyin_submit) 
Buyin_entry.grid(row=4, column=1, pady = 10)
Buyin_entry.config(bg='light blue')

Bet_entry = tk.Button(root, text='Submit bet', font=('Helvetica', '10'), command=bet_submit) 
Bet_entry.grid(row=4, column=3, pady = 10)
Bet_entry.config(bg='light blue')

unavailable()

if __name__ == "__main__":
    root.mainloop()
