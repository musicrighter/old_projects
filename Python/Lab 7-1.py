# David Gustafson Lab 7-1

import turtle

def get_ok():
    ok = ''
    while ok != 'y' and ok != 'n':
        ok = input('Do again? Press y or n: ')
        ok.lower() + ' '
        ok = ok[0]
    return ok

def get_float(prompt):
    temp = input(prompt + ': ')
    return float(temp)

def get_int(prompt):
    msg = prompt + ': '
    temp = input(msg)
    return int(temp)

more = 'y'
while more == 'y':
    turtle.reset()
    turtle.bgcolor('Dark green')
    angle = get_float('Turn angle (91-160, works OK, 98, 135.1, 144.2 work well)')
    number_of_lines = get_int('Draw how many lines (300-1000 work well)')

    for i in range(number_of_lines):
        turtle.speed = 0
        turtle.color('yellow')
        turtle.forward(i)
        turtle.right(angle)

    more = get_ok()

print('Finished')
        
