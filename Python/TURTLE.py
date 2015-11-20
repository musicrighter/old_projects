import turtle

def get_ok():
    ok = ''
    while ok != 'y' and ok != 'n':
        ok = input('Do again? Press y or n ')
        ok.lower() + ' '
        ok = ok[0]
    return ok

def get_int(prompt_message):
    msg = prompt_message + ' '
    temp = input(msg)
    return int(temp)

def get_float(prompt_message):
    temp = input(prompt_message + ' ')
    return float(temp)

def draw_triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)

def invisible_move(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()

more = 'y'
while more == 'y':
    turtle.reset()
    turtle.bgcolor('blue')
    turtle.color('red', 'yellow')
    speed = get_int('Turtle speed 1 very slow - 9 fast or 0 fastest:')
    turtle.speed(speed)
    size = get_float('Starting size of side of figure (100 - 300 work well)')
    angle = get_float('Turn angle (1 to 20 work well)')
    smaller = get_float('How much smaller for each figure (1 to 20 work well)')
    move = get_float('How far to offset each figure (1 to 20 work well)')
    number_of_items = get_int('How many to draw (100 to 700 work well)')
    
    for i in range(number_of_items):
        if i > 19:
            turtle.speed = 0
        turtle.begin_fill()
        draw_triangle(size) 
        invisible_move(move)
        turtle.left(angle)
        size = size - smaller
        if size <= 1:
            break
        turtle.end_fill()
    more = get_ok()


'''        
favorites = []
x = 98.0
favorites.append(x)
y = 135.6
favorites.append(y)
for item in favorites:
    print(item)
'''














    
