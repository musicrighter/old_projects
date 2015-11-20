import tkinter as tk
from tkinter.messagebox import showinfo


def everything():
	global names, new_names, colors

	other = tk.Tk()
	other.title('Choose a user profile or Make Your Own!')
	other.configure(bg='light blue')

	names = ['Joey', 'Mom', 'Michaela', 'Dad', 'None']
	new_names = []
	colors = ['red', 'dark green', 'purple', 'blue', 'orange']

	def person(x):
		global name, dealer_wins, player_wins, balance, password, good
		with open('people.txt', 'r') as my_file:
			for line in my_file:
				line = (line.strip()).split()
				name, dealer, player, amount, password = line
				if x == name:
					name = name
					dealer_wins = int(dealer)
					player_wins = int(player)
					balance = int(amount)
					password = str(password)
					if password != '0':
						people(dis=True)
						new_people(dis=True)
						password_func()
						return
					ok['state'] = 'normal'
					reset['state'] = 'normal'
					delete['state'] = 'normal'
					return

	def password_func(new=False):
		global phrase_input
		phrase = tk.Label(other, text='Password:', font=('Helvetica', '12'))
		phrase.grid(row=6 + (x//5), column=0, columnspan=2, padx=10) 

		phrase_input = tk.Entry(other, font=('Helvetica', '12'))
		phrase_input.grid(row=6 + (x//5), column=1, columnspan=3) 

		if new == False:
			function = correct
		else:
			function = pass_set

		phrase_enter = tk.Button(other, text='Enter password', font=('Helvetica', '12'), command=function)
		phrase_enter.grid(row=6 + (x//5), column=3, columnspan=3, padx=10)

	def pass_set():
		name = user.get().title()
		count = 0
		with open('people.txt', 'r') as my_file:
			data = my_file.readlines()
			for line in data:
				line = (line.strip()).split()
				person, dealer, player, amount, password = line
				if name == person:
					dealer = 0
					player = 0
					amount = 0
					password = phrase_input.get() 
					if password == '':
						password = 0
					data[count] = str(name) + ' ' + str(dealer) + ' ' + str(player) + ' ' + str(amount) + ' ' + str(password) + '\n'

					with open('people.txt', 'w') as last_file:
						last_file.writelines(data)
					other.destroy()
					everything()
					return
				count += 1

	def correct():
		global phrase_input, good, password
		entry = phrase_input.get()
		if entry == password:
			ok['state'] = 'normal'
			reset['state'] = 'normal'
			delete['state'] = 'normal'
		else:
			showinfo('You big fat phony!!!', 'Wrong password')
			good = False
			other.destroy()

	def people(dis=False):
		global names
		n = 0
		for x in names:
			one = tk.Button(other, text=x, font=('Helvetica', '12', 'bold'), command=lambda x=x: person(x)) 
			one.grid(row=2, column=n, padx = 5, pady = 10)
			one['bg'] = colors[n]
			one['fg'] = 'white'
			one['width'] = 7
			if dis == True:
				one['state'] = 'disabled'
				new['state'] = 'disabled'
			n += 1

	def new_people(dis=False):
		global new_names, x
		x = 0
		c = 0
		for p in new_names:
			two = tk.Button(other, text=p, font=('Helvetica', '12', 'bold'), command=lambda p=p: person(p)) 
			two.grid(row=3 + (x//5), column=c, padx = 5, pady = 10)
			two['bg'] = colors[c]
			two['fg'] = 'white'
			two['width'] = 7
			if dis == True:
				two['state'] = 'disabled'
				new['state'] = 'disabled'
			x += 1
			c += 1
			if c == 5:
				c = 0

	def stop():
		global good
		good = True
		other.destroy()

	def create():
		person = user.get().title()
		if person == '':
			person = 'Name?'

		with open('people.txt', 'a') as out_file:
			out_line = person.title() + ' ' + str(0) + ' ' + str(0) +  ' ' + str(0) + ' ' + str(0) + '\n'
			out_file.write(out_line)

		password_func(new=True)
		# other.destroy()
		# everything()

	def reset():
		global name
		count = 0
		with open('people.txt', 'r') as my_file:
			data = my_file.readlines()
			for line in data:
				line = (line.strip()).split()
				person, dealer, player, amount, password = line
				if name == person:
					data[count] = str(name) + ' ' + str(0) + ' ' + str(0) + ' ' + str(0) + ' ' + str(0) + '\n'

					with open('people.txt', 'w') as last_file:
						last_file.writelines(data)
					other.destroy()
					everything()
					return
				count += 1

	def delete():
		global name, new_names
		count = 0
		with open('people.txt', 'r') as my_file:
			data = my_file.readlines()
			for line in data:
				line = (line.strip()).split()
				person, dealer, player, amount, password = line
				if name == person:
					del data[count]

					with open('people.txt', 'w') as last_file:
						last_file.writelines(data)
					other.destroy()
					everything()
					return
				count += 1

	with open('people.txt', 'r') as my_file:
			counter = 0
			for line in my_file:
				line = (line.strip()).split()
				added, dealer, player, amount, password = line
				if counter > 4:
					new_names.append(added)
				counter += 1

	people()
	new_people()


	choice = tk.Label(other, text='Please select a user profile from below', font=('Helvetica', '14', 'bold'))
	choice.grid(row=0, column=0, columnspan=5, padx = 10, pady = 10) 
	choice.config(bg='light blue')

	first = tk.Label(other, text='First name:', font=('Helvetica', '12'))
	first.grid(row=4 + (x//5), column=0, columnspan=2, padx = 10, pady = 10) 
	first.config(bg='light blue')

	user = tk.Entry(other, font=('Helvetica', '12'))
	user.grid(row=4 + (x//5), column=1, columnspan=3) 

	new = tk.Button(other, text='Create new user', font=('Helvetica', '12'), command=create)
	new.grid(row=4 + (x//5), column=3, columnspan=3)
	new.config(bg='light blue')

	ok = tk.Button(other, text='OK', font=('Helvetica', '14', 'bold'), command=stop)
	ok.grid(row=5 + (x//5), column=2)
	ok.config(bg='black')
	ok['fg'] = 'white'
	ok['state'] = 'disabled'

	reset = tk.Button(other, text='Reset profile', font=('Helvetica', '12'), command=reset)
	reset.grid(row=5 + (x//5), column=0, columnspan=2)
	reset.config(bg='light blue')
	reset['state'] = 'disabled'

	delete = tk.Button(other, text='Delete profile', font=('Helvetica', '12'), command=delete)
	delete.grid(row=5 + (x//5), column=3, columnspan=2)
	delete.config(bg='light blue')
	delete['state'] = 'disabled'

	other.mainloop()

	return name, dealer_wins, player_wins, balance, password, good
