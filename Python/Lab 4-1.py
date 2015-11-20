# David Gustafson, Lab 4-1

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

limit = 10

do_again = 'y'

while do_again == 'y':
    x = get_int('Enter x as a number from -10 to 20')
    if limit < x:
        print('Yes!', limit, 'less than', x)
    else:
        print('No..', limit, 'not less than', x)
    do_again = input('Try another? (y or n) ')
    

# x = 9, returns 'No.. 10 not less than 9'
# x = 10, returns 'No.. 10 not less than 10'
# x = 11, returns 'Yes! 10 less than 11'
