"""
alphacode.py:  CIS 210 assignment 1, Winter 2014
author: David Gustafson

Convert 4-digit PIN to alphabetic code
"""

c_list = "bcdfghjklmnpqrstvwyz" 
v_list = "aeiou"  

import sys
if (len(sys.argv) > 1) :
    pincode = int(sys.argv[1])
else :
    print("Usage: python3 alphacode 9999")
    exit(1)  

high = pincode // 100
low = pincode % 100

vowel2 = low % 5
con2 = low // 5
vowel1 = high % 5
con1 = high // 5

v1 = v_list[vowel1]
c1 = c_list[con1]
v2 = v_list[vowel2]
c2 = c_list[con2]

pincode = str(c1 + v1 + c2 + v2)

print("Encoding of", sys.argv[1], 'is',  pincode)


