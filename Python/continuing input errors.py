import math

pi = math.pi

def get_ok():
    result = input('Would you like to continue? ')
    answer = result.lower()
    return answer[0]
     
def circle_area(r):
    area = pi*r**2
    return round(area, 2)

def circle_c(r):
    c = 2*pi*r
    return round(c, 2)

ok = 'y'
while ok == 'y':
    radius = float(input('Enter radius: '))
    print('The area is:', circle_area(radius))
    print('The circumfrance is:', circle_c(radius))
    ok = get_ok() 
    print()

# Do This 
''''''''''''''''|
input()         |
astring.lower() |
len(astring)    |
astring[0]      |
'''''''''''''''''
