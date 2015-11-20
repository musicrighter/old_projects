# David Gustafson, Lab 4-6

points = float(input('Please enter the total points:\n'))

if points >= 50:
    grade = 'S ("Superstar")'
elif points >= 40:
    grade = 'A'
elif points >= 30:
    grade = 'B'
elif points >= 25:
    grade = 'C'
else:
    grade = 'Z'

print(points, grade)
