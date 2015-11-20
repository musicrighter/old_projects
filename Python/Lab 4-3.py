# David Gustafson, Lab 4-3

def get_int(promp_message):
    '''(str) -> int
        displays prompt message,
        gets input from user
        converts input string to number,
        returns number to caller
    '''
    prompt = promp_message + ' '
    temp = input(prompt)
    return int(temp)

def get_float(promp_message):
    '''(str) -> float
        displays prompt message,
        gets input from user
        converts input string to number,
        returns number to caller
    '''
    prompt = promp_message + ' '
    temp = input(prompt)
    return float(temp)

limit = 10

do_again = 'y'

while do_again == 'y':
    x = get_float('Enter x as a number from -10 to 20')
    if limit < x:
        print('Yes!', limit, 'is less than', x)
    elif limit <= x:
        print('Yes!', limit, 'is less than or equal to', x)
    elif limit == x:
        print('Yes!', limit, 'is equal to', x)
    elif limit != x:
        print('No..', limit, 'is not equal to', x)
    else:
        print('No..', limit, 'is not less than', x)
    do_again = input('Try another? (y or n) ')
    


