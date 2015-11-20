# David Gustafson Lab 7 Extra Credit 1

import turtle

def get_ok():
    ok = ''
    while ok != 'y' and ok != 'n':
        ok = input('Do another? Press y or n: ')
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
        answer = answer.lower() + 'x'
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
print('\nFavorites List:')
for angle in favorites:
    print('Number', str(count) + ', Picture from angle', angle)
    count += 1

more = 'y'

if y_or_n('Would you like to see an image?') == 'y':    
    while more == 'y':
        num = int(input('Which number out of the favorites list?: '))
        turtle.reset()
        for i in range(100):
            turtle.speed = 0
            turtle.color('yellow')
            turtle.forward(i)
            turtle.right(favorites[num])

        more = get_ok()

print('Finished')
        
