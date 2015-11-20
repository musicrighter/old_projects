import random

def lottery():
    winnings = 0

    x = random.randint(1, 3)
    y = random.randint(1, 3)

    if x == y:
        print('You won $100!')
        winnings += 100
    else:
        print('Not a winner, but try again for $20')
        winnings -= 20

    print('Your winnings so far:', winnings, '\n')


print('LOTTERY GAME!')
print()


a = input('Would you like to play, if yes then press enter\n')

if a == 'no':
    print('Have a good day!')

while True:
    b = input('Would you like to continue for $20\n')

    if b != 'no':
        lottery()

    else:
        print('Thanks anyways')



    


    
