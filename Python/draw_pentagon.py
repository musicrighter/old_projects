import turtle

def draw_pentagon(x):
    n_sides = 5
    angle = 360/n_sides
    for i in range(n_sides):
        turtle.forward(x)
        turtle.left(angle)

length = int(input('Please enter a side length: '))
draw_pentagon(length)
