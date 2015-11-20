# David Gustafson Lab 7 Extra Credit 2

import turtle

def get_ok():
    ok = ''
    while ok != 'y' and ok != 'n':
        ok = input('Do again? Press y or n: ')
        ok.lower() + ' '
        ok = ok[0]
    return ok

def draw_polygon(length, n_sides):
    angle = 360 / n_sides
    for i in range(n_sides):
        turtle.forward(length)
        turtle.right(angle)

def invisible_move(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()

def get_int(prompt_message):
    msg = prompt_message + ' '
    temp = input(msg)
    return int(temp)

def get_float(prompt_message):
    temp = input(prompt_message + ' ')
    return float(temp)

more = 'y'
while more == 'y':
    turtle.reset()
    turtle.bgcolor('Dark green')
    n_sides = get_int('Please enter a number of sides:')
    length = get_int('Please enter a side length (100 - 300 work well):')
    angle = get_float('Turn angle (1 to 20 work well):')
    smaller = get_float('How much smaller for each figure (1 to 20 work well)')
    move = get_float('How far to offset each figure (1 to 20 work well):')
    n_lines = get_int('How many lines to draw (100 to 700 work well):')
    
    for i in range(n_lines):
        turtle.color('blue', 'red')      
        turtle.begin_fill()              # I've found that these work well:
        turtle.speed = 0
        draw_polygon(length, n_sides)    # L = 200, N_S = 5
        invisible_move(move)             # M = 3
        turtle.left(angle)               # A = 10
        length = length - smaller        # S = 3
        if length <= 1:
            break
        turtle.end_fill()

        turtle.color('blue', 'yellow')
        turtle.begin_fill()
        turtle.speed = 0
        draw_polygon(length, n_sides) 
        invisible_move(move)
        turtle.left(angle)
        length = length - smaller
        if length <= 1:
            break
        turtle.end_fill()
        
    more = get_ok()
