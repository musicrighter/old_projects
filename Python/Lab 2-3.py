# By David Gustafson
# Lab 2-3.py

import turtle

def draw_triangle(size):
    '''Draws an equilateral triangle
       The only input argument the function takes is "size"
       The turtle points in a different direction
       every time it turns left(120)
    '''
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

draw_triangle(100)

a = 50
draw_triangle(a)
draw_triangle(a + 20)

turtle.forward(60)

length = 150
for i in range(8):
    draw_triangle(length)
    length = length + 15

    
    

