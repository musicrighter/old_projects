"""
jumbler.py:  CIS 210 assignment 2a, Winter 2014
author: David Gustafson

Find words from a txt file that match a scrambled word input
"""

import sys

USAGE = '''
Usage: python jumbler.py jumbled_word wordlist.txt
Please enter both a jumbled word and a file to open
'''
 
if len(sys.argv) != 3:
    print(USAGE)
    exit(1)
jumble = sys.argv[1]
sorted_jumble = ''.join(sorted(jumble)) # Alphabatize input and join letters
file = sys.argv[2]
words = open(file) # open word list file

match_num = 0
file_num = 0

for line in words:
    file_num += 1
    word = line.strip() # Chop off newline
    sorted_word = ''.join(sorted(word)) # Alphabatize word and join letters
    if sorted_word == sorted_jumble:
        print(word)
        match_num += 1

if match_num == 1:
    print(match_num, 'match from', file_num, 'words') 
else:
    print(match_num, 'matches from', file_num, 'words')
