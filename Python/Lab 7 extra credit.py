# David Gustafson Lab 7 Extra Credit

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

def y_or_n(question):
    answer = ''
    while answer != 'y' and answer != 'n':
        answer = input(question + ' Press y or n: ')
        answer =answer.lower() + 'x'
        answer = answer[0]
    return answer

favorites = []

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

    save_favorite = y_or_n('Save this picture as a favorite?')
    if save_favorite == 'y':
        favorites.append(angle)

    more = get_ok()

count = 0
print('Favorites List:')
for angle in favorites:
    print('#' + str(count) + ', Picture from angle', angle)
    count += 1

print('Finished')
        
