debaters = [['Jake', 4], ['Jill', 2], ['Bob', 2], ['Alice', 0], ['Kelly', 3]]

biggest = 0
who = ''
winning_list = []

for sublist in debaters:
    if sublist[1] > biggest:
        biggest = sublist[1]
for sublist in debaters:
    if sublist[1] == biggest:
        winning_list.append(sublist[0])
    
print('Winning score is', biggest)
print('Winning student(s):')
for student in winning_list:
    print(student)
