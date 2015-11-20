student = get_name()
country = get_country()
if country == 'China' or country == 'India':
    print(student, '*')
else:
    print(student)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#exclusive or x < a or x > b but not both

if(x < a) or (x > b):
    if not(x < a and x > b):
        print('just one condition is true')

aCondition = x < a
bCondition = x > b

if aCondition != bCondition:
    print('just one condition is true')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Substitution Principles:

a = 7       # sub var for #
b = a + 4

if a > b:
    print('Hi')

c = a > b
if c:
    print('Hi')


animal = cat
zoo = 'We have a ' + 'cat'


Define a function
.---------------.
|1 function     |
|does           |
|1 simple task  |
'---------------'

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''







