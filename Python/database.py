from sqlite3 import*

def capcase(s):
	return s.title()

db = connect('sakila.db')

db.create_function('capitalized', 1, capcase)
db.execute('UPDATE film SET title = capitalized(title)')

db.commit() 



# for x in db.execute('select title from film limit 5'):
# 	print(x)