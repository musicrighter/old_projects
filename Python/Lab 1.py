# David Gustafson, Lab 1

import sys
def greetings():
    print('Hi')
    return 'Hello, World'

print(greetings())

def test1(n):
    return n*n

n = sys.argv[1]
print(test1(n))

