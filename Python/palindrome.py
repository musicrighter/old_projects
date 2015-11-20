# David Gustafson

# I will figure out how get and copy the user input
# I will clean out the non-letters and create a copy 
# of the cleaned input with letters in reversed order.

n = input("Enter the String:\n")
def palindrome(n):
    index=0
    check=True
    while index<len(n):
        if n[index]==n[-1-index]:
            index+=1
            return True
        return False
if palindrome(n)==True:
    print(n, "is a Palindrome")
else:
    print(n, "is not a Palindrome")
