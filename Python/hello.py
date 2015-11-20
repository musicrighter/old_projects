"""
   David Gustafson hello.py
   CIS 211, Spring 2014

   A program that displays a 'hello, world' message in any of the languages displayed on the buttons.
   When a button is clicked, the message changes to the equivalent in that language.
"""
import tkinter as tk
root = tk.Tk()

def span():
	hello.configure(text='Hola mundo')

def fren():
	hello.configure(text='Bonjour tout le monde')

def ital():
	hello.configure(text='Ciao mondo')

hello = tk.Label(root, text="hello, world")
hello.grid(row=0, column=0, columnspan=3)

sbutton = tk.Button(root, text='Spanish', command=span) 
sbutton.grid(row=2, column=0, padx = 10, pady=10)

fbutton = tk.Button(root, text='French', command=fren) 
fbutton.grid(row=2, column=1, padx = 10, pady=10)

ibutton = tk.Button(root, text='Italian', command=ital) 
ibutton.grid(row=2, column=2, padx = 10, pady=10)

quit = tk.Button(root, text='Quit', command=quit) 
quit.grid(row=3, column=1, pady = 10)

if __name__ == "__main__":
    root.mainloop()