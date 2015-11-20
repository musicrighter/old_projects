"""
   David Gustafson payment.py
   CIS 211, Spring 2014

   A program that calculates the monthly payment of a loan based on the inputted 
   Loan amount, Interest rate, and Years.
"""
import tkinter as tk

root = tk.Tk()

def convert():
	payment['state'] = 'normal'
	rtext = float(rate.get())
	ytext = float(years.get())
	atext = float(amount.get())
	r = rtext/100/12
	p = 12 * ytext
	pay = (r*atext)/(1-(1+r)**(-p)) 
	pay = str(round(pay, 2))
	payment.delete(0, tk.END)
	payment.insert(0, '$' + pay)
	payment['state'] = 'readonly'

alabel = tk.Label(root, text="Loan amount:")
alabel.grid(row=0, column=0, sticky=tk.W, padx = 20, pady = 10)

rlabel = tk.Label(root, text="Interest rate:")
rlabel.grid(row=1, column=0, sticky=tk.W, padx = 20, pady = 10)

ylabel = tk.Label(root, text="Years:")
ylabel.grid(row=2, column=0, sticky=tk.W, padx = 20, pady = 10)

amount = tk.Entry(root)
amount.grid(row=0, column=1, padx = 20)

rate = tk.Entry(root)
rate.grid(row=1, column=1, padx = 20)

years = tk.Entry(root)
years.grid(row=2, column=1, padx = 20)

payment = tk.Entry(root)
payment.grid(row=3, column=1, pady = 40)

button = tk.Button(root, text='Monthly payment:', command=convert) 
button.grid(row=3, column=0, pady = 40)

if __name__ == "__main__":
    root.mainloop()