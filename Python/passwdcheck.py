"""
passwdcheck.py: CIS 210 assignment 1, Winter 2014
authors: David Gustafson

Check that password is 8-32 contains required elements:
  Upper case letters
  Lower case letters
  Digits
"""

import sys
if (len(sys.argv) > 1) :
    passwd = sys.argv[1]
else:
    print("Usage: python3 passwdcheck.py 9999")
    exit(1)

upper = False
lower = False
digit = False
six = False

for character in passwd:
    if character.isupper():
        upper = True 
    if character.islower():
        lower = True
    if character.isdigit():
        digit = True

if len(passwd) >= 6:
    six = True

if lower == False:
    print("Password must include lower case letters")
if upper == False:
    print("Password must include upper case letters")
if digit == False:
    print("Password must include digits")
if six == False:
    print("Password must be at least 6 characters long")
if upper and lower and digit and six == True:
    print("Good password")

