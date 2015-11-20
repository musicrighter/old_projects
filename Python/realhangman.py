import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
 \O/  |
  |   |
 < >  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',]

print('| H A N G M A N |')
print('-' * 17)

choice = input('''Which language would you like to use?
English(e), French(f), German(g), or Italian(i): ''')
print()

choice = choice.lower()[0]

if choice == 'e':
    lang = 'englishwords.txt'
elif choice == 's':
    lang = 'spanish_words.txt'
elif choice == 'f':
    lang = 'french_words.txt'
elif choice == 'g':
    lang = 'german_words.txt'
elif choice == 'i':
    lang = 'italian_words.txt'

words = []
with open(lang, 'r') as my_file:
        words = []
        for line in my_file:
            line = line.strip()
            words.append(line)

easy = []
medium = []
hard = []
crazy = []
for i in words:
    if len(i) <= 4:
        easy.append(i)
    elif len(i) < 7:
        medium.append(i)
    elif len(i) < 10:
        hard.append(i)
    elif len(i) >= 10:
        crazy.append(i)
        
words1 = '''ant baboon badger bat bear beaver camel cat clam cobra
cougarcoyote crow deer dog donkey duck eagle ferret foxfrog goat goose
hawk lionlizard llama mole monkey moose mousemule newt otter owl panda
parrot pigeonpython rabbit ram ratraven rhino salmon seal shark sheep
skunk sloth snakespiderstork swan tiger toad trout turkey turtle weasel
whale wolf wombat zebra'''.split()

wins = 0
losses = 0
chances = 9

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)): 
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks: 
        print(letter, end=' ')
    print()
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in "abcdefghijklmnopqrstuvwxyz'":
            print('Please enter a LETTER.')
        else:
            return guess
def playAgain():
    again = input('Do you want to play again? (yes or no): ')
    print()
    return again.lower().startswith('y')

def percent(losses, wins):
    return str(int(100 * (wins / (losses + wins))))+ '%'

def score():
    print('-' * 28)
    if wins == 1:
        print(wins, 'win, ', end='')
    else:
        print(wins, 'wins, ', end='')
    if losses == 1:
        print(losses, 'loss ... ', end='')
    else:
        print(losses, 'losses ... ', end='')
    print(percent(losses, wins))
    print('-' * 28)
    
missedLetters = ""
correctLetters = "'"
level = input('Easy(e), Medium(m), Hard(h), or Crazy(c)?: ').lower()[0]
if level == 'e':
    dif = easy
elif level == 'm':
    dif = medium
elif level == 'h':
    dif = hard
elif level == 'c':
    dif = crazy
secretWord = getRandomWord(dif)
gameIsDone = False
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('\nYes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
            wins += 1
            score()
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!')
            print('After',len(missedLetters), 'missed guesses and', len(correctLetters), 'correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
            losses += 1
            chances -= 1
            score()
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            level = input('Easy(e), Medium(m), Hard(h), or Crazy(c)?: ').lower()[0]
            if level == 'e':
                dif = easy
            elif level == 'm':
                dif = medium
            elif level == 'h':
                dif = hard
            elif level == 'c':
                dif = crazy
            secretWord = getRandomWord(dif)
        else:
            break
