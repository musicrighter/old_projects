import sys

user_input = sys.stdin.readline()   # Get
user_input = user_input.strip()     # user
user_input = user_input.split()     # imput

num_half = int(user_input[1])       # set variables
num_double = int(user_input[0])
answer = 0

while num_half != 0:    
    if num_half % 2 == 1 and num_half != 2:   # skips even numbers
        print('Halving:', int(num_half))
        print('Doubling:', num_double)
        answer += num_double
    num_half = num_half // 2
    num_double = num_double * 2

print('Answer:', answer)
