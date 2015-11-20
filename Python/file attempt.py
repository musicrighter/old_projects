names = []
ages = []

print('Writing to file name "name_and_age.txt"')

more = 'y'
while more == 'y':
    name = input('\nWhat is your name?: ').lower()
    names.append(name.capitalize())
    age = input('What is your age?: ')
    ages.append(age)

    more = input('\nAnother person? Press y or n: ')
    more = more.lower()[0]

with open('name_and_age.txt', 'a') as out_file:
    for i in range(len(names)):
        name = names[i]
        age = str(ages[i])
        out_line = name + ',' + age + '\n'
        out_file.write(out_line)

with open('name_and_age.txt', 'r') as my_file:
    for line in my_file:
        print(line.strip())

print('\nFinished')





    
