# David Gustafson, Lab 5-2

print('Tiny National Bank of Walterville')
print('Credit Card Payments\n')

def min_payment(balance):
    '''This function takes the inputed balance and figures out
       what the minimum payment should be. It returns the value
       of the minimum payment back into the main body.
    '''
    percent = balance * 0.027
    if balance <= 0:
        payment = 'Your balance is current, no payment is needed.'
    elif percent < 12 and balance > 12:
        payment = float(12)
    elif percent > 12 and percent < balance:
        payment = round(percent, 2)
    elif balance < 12:
        payment = balance
    return payment
    
again = 'y'

while again == 'y':
    balance = float(input('Credit card balance? '))
    payment = min_payment(balance)
    print('Minimum payment due: $' + str(payment), '\n')
    again = input('Another customer (y or n)? ')
    print()

