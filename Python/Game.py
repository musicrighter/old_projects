
import random

guesses_made = 0

name = input('Hello! What is your name?\n')

number = random.randint(1, 20)
print()
print ('Well, I am thinking of a number between 1 and 20.')

while guesses_made < 6:

    guess = int(input('Take a guess: '))

    guesses_made += 1

    if guess < number:
        print ('Your guess is too low.')

    if guess > number:
        print ('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    print()
    print('Good job', name + '!')
    print('You guessed my number in', guesses_made, 'guesses!')
else:
    print()
    print('Sorry', name, 'the number I was thinking of was', number)
