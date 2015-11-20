# David Gustafson, Lab 5-1

print('Tiny National Bank of Walterville')
print('Credit Card Payments\n')

def payment(rounded_balance):
    percent = float(rounded_balance * 0.027)
    if percent < float(12):
        return True
    elif percent > float(12):
        return False
    return percent
    
again = 'y'

while again == 'y':
    balance = float(input('Credit card balance? '))
    rounded_balance = round(balance, 2)
    if payment(rounded_balance) == True:
        payment = '12.00'
    elif payment(rounded_balance) == False:
        payment = round(percent, 2)
    print('Minimum payment due: $' + payment, '\n')
    again = input('Another customer (y or n)? ')
    print()

