# David Gustafson, Lab 4-5

name = 'argon'

do_again = 'y'

while do_again == 'y':
    letter = input('Enter a letter or word:\n')

    # I know that these next few tests won't work,
    # but i'm not sure what else to put in this lab

    if name == 14:
        print('Yes!', name, "is equal to 14")
    elif name < 14:
        print('Yes!', name, "is less than 14")
    elif name != 14:
        print('No..', name, 'is not equal to 14')
    else:
        print('No..', name, 'is not less than 14')
    do_again = input('Try another? (y or n) ')
    


