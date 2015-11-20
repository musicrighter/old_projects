import random

print('LOTTERY GAME!')
print()

winnings = 0

a = input('Would you like to play, if yes then press enter\n')

if a == 'no':
    print('Have a good day!')

while True:
    b = input('Continue?\n')

    if b != 'no':
        x = random.randint(1, 4)
        y = random.randint(1, 4)

        if x == y:
            print('You won $100!')
            winnings += 100
        else:
            print('Try again for $20')
            winnings -= 20

        print('Winnings so far:', winnings, '\n')

    else:
        print('Thanks anyways')



    


    
