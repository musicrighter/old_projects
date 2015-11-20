import turtle

size = 40
x = 70

def draw_square(size):
    angle = 360 / 4
    for i in range(4):
        turtle.forward(size)
        turtle.left(angle)
    return
