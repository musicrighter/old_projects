x = int(input('What was your score?:\n'))

if x > 100:
    grade = 'A+, Amazing!'
elif x >= 90:
    grade = 'A, good job!'
elif x >= 80:
    grade = 'B'
elif x >= 70:
    grade = 'C'
elif x >= 60:
    grade = 'D'
elif x <= 59:
    grade = 'F, sorry'
elif x < 0:
    print('Please enter a number above 0')

print(grade)
 
