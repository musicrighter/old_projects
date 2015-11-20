import tkinter as tk
from tkinter import Frame

class Car:
	def __init__(self, capacity, mpg):
		self._capacity = capacity
		self._mpg = mpg
		self._tank = 0

	def __repr__(self):
		return str([self._tank, self._capacity, self._mpg])

	def fill(self):
		self._tank = min(self._capacity, self,_tank + gallons)

	def drive(self, miles):
		fuel_needed = miles / self._mpg
		if fuel_needed > self._tank:
			self._tank = 0
			return self._tank * self._mpg
		else:
			self._tank -= fuel_needed
			return miles

	def level(self):
		return self._tank

class MPGFrame(Frame):

	def __init__(self, capacity, mpg):
		Frame.__init__(self)
		self.grid()

		self._car = Car(capacity, mpg)
		self._max = capacity

		self._fill_button = Button(self, text='Fill', command=self.fill_it)
		self._fill_button.grid(row=1, column=0)
		self._fill_entry = Entry(self, width=5)
		self._fill_entry.grid(row=1, column=1)
		self._drive_button = Button(self, text='Drive', command=self.drive_it)
		self._drive_button.grid(row=2, column=0)
		self._drive_entry = Entry(self, width=5)
		self._drive_entry.grid(row=2, column=1)

		Label(self, text='Fuel level').grid(row=3, column=0)
		self._level = Label(self, text=str(self._car.level()))
		self._level.grid(row=3, column=1)

	def fill_it(self):
		amt = float(self._fill_entry.get())
		if amt + self._car.level() > self._max:
			showinfo('Refill error', "The car doesn't hold that much gas")
		else:
			self._car.fill(amt)
			self._level.configure(text=str(self._car.level()))

	def drive_it(self):
		miles = float(self._drive_entry.get())
		if miles / self._mpg > self._tank:
			showinfo('Miles error', "The car doesn't have that much gas")
		else:
			self._car.drive(miles)
			self._level.configure(text=str(self._car.level()))

# root1 = tk.Tk()
root = MPGFrame(12, 30)

if __name__ == "__main__":
    root.mainloop()