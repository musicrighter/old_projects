import random

guessesTaken = 0 
 
myName = input('Hello! What is your name?\n')
 
number = random.randint(1, 20) 
print('Well, ' + myName + ', I am thinking of a number between 1 and 20') 

while guessesTaken < 6: 
    print('Take a guess.')
    
    guess = int(input()) 
 
    guessesTaken += 1 

    if guess < number: 
        print('Your guess is too low.')  
 
    if guess > number: 
        print('Your guess is too high.') 

    if guess == number: 
        break 

if guess == number:
        print('Good job,', myName + '! You guessed my number in',
guessesTaken, 'guesses!') 
    
if guess != number: 
        print('Sorry, the number I was thinking of was', number)
