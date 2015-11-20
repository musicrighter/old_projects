# David Gustafson Lab 3-6

# I will figure out how get and copy the user input.
# I will clean out the non-letters and create a copy 
# of the cleaned input with letters in reversed order.

# I will compare the cleaned input and reversed phrase
# to determine if the input is a palindrome.
# Then print the original string, cleaned string, reversed
# string and if the input is a palindrone or not.

def clean_string(a_lot_of_letters):
    '''(str) -> str
       copies only lowercase alphabet letters to new string
       return new string to caller

       >>>clean_string('look out!')
       lookout
    '''
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for letter in a_lot_of_letters:
        if letter in alphas:
            print('About to add', letter, 'to', new_string)
            new_string = new_string + letter
    print("Cleaning string")
    return new_string

def reverse_string(string):
    print('reversing the string')
    new_add_before = ''
    for letter in clean_phrase:
        new_add_before = letter + new_add_before
    reverse = new_add_before
    return reverse

original_string = input('Enter a phrase in lower case please: ')
print('Original string:', original_string)

clean_phrase = clean_string(original_string)
print('Cleaned string:', clean_phrase)

reverse_phrase = reverse_string(clean_phrase)

print()
print('Cleaned:', clean_phrase, '\nReversed:', reverse_phrase)
print()

if clean_phrase == reverse_phrase:
    print("It's a palindrome -- reads the same forward as backwards!")
else:
    print('Sorry, not a palindrome')
print('The end')
