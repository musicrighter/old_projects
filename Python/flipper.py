"""
   David Gustafson flipper.py
   CIS 211, Spring 2014

   A program that displays a combination of card backs, card fronts, or blank backgrounds.
   When the flip button is pressed, it cycles through to the next card.
"""
import tkinter as tk
from random import randint
from CardLabel import *

sides = ['back', 'front', 'blank']
n = 1
x = 0

def flip():
	global n, x
	card = [one, two, three]
	if x == 3:
		n = (n + 1) % 3
		x = 0
	card[x].display(sides[n], randint(0,51))
	x += 1

root = tk.Tk()
CardLabel.load_images()

root.rowconfigure(0, minsize=130)
for i in range(3):
	root.columnconfigure(i, minsize=100)

one = CardLabel(root)
one.grid(row=0, column=0, padx = 10, pady = 10)

two = CardLabel(root)
two.grid(row=0, column=1, padx = 10, pady = 10)

three = CardLabel(root)
three.grid(row=0, column=2, padx = 10, pady = 10)

button = tk.Button(root, text='Flip', command=flip) 
button.grid(row=1, column=1, pady = 10)


if __name__ == "__main__":
    root.mainloop()