# David Gustafson Lab-6

import math
pi = math.pi

def get_ok():
    ''' () -> str
        returns 'y' or 'n' typed in by user
    '''
    ok = input('Do again? Press y or n: ')
    print()
    ok = ok.lower()
    if len(ok) > 1:
        ok = ok[0]
    return ok

def circle_area(radius):
    area = pi * square(radius)
    return round(area, 2)

def cylinder_volume(radius, height):
    volume = (pi * square(radius)) * height
    return round(volume, 2)

def get_float(prompt_message):
    temp = input(prompt_message + ': ')
    return float(temp)
    

def float_money(amount):
    dollars_string = format(amount, ',.2f')
    return dollars_string

def square(x):
    return x * x

def tax(price):
    tax = price * 0.015698
    return round(tax, 2)


ok = 'y'
while ok == 'y':
    my_radius = get_float('Enter radius of circle')
    area = circle_area(my_radius)
    print('Area of circle', circle_area(my_radius), 'with radius', my_radius)
    print()

    my_height = get_float('Enter height of cylinder')
    volume = cylinder_volume(my_radius, my_height)
    print('Volume of cylinder', volume)
    print()

    home_price = get_float('Enter home price')
    display_price = float_money(home_price)
    print('Home for sale, price is $' + display_price)
    tax = tax(home_price)
    property_tax = float_money(tax)
    print('Property Tax is $' + property_tax)
    print()

    ok = get_ok() 










    
