# David Gustafson, Lab 4 extra credit

do_again = 'y'

while do_again == 'y':
    income = float(input('Please enter your Annual Income: '))

    if income > 277000:
        rate = 3.0
        tax = 0.030
    elif income == 277000:
        rate = 2.7
        tax = 0.027
    elif income >= 112450:
        rate = 2.2
        tax = 0.022
    elif income >= 75000:
        rate = 1.8
        tax = 0.018
    elif income >= 47300:
        rate = 1.4
        tax = 0.014
    elif income >= 22400:
        rate = 1.0
        tax = 0.010
    elif income >= 17500:
        rate = 0.6
        tax = 0.006
    elif income >= 15000:
        rate = 0.5
        tax = 0.005
    else:
        rate = 0
        tax = 0

    tax_due = income * tax

    print()
    print('Income:', income)
    print('Rate:', rate, 'percent')
    print('Tax Due:', tax_due)
    do_again = input('Would you like to enter another value? (y or n): ')
