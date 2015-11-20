# David Gustafson, Lab 4-7

do_again = 'y'

while do_again == 'y':
    age = int(input('Please enter your age: '))
    bmi = float(input('Please enter your BMI: '))

    young = age < 45
    slim = bmi < 0.22

    if young and slim:
        risk = 'Low'
    elif young and not slim:
        risk = 'Moderate'
    elif not young and slim:
        risk = 'Moderate'
    else:
        risk = 'High'

    print()
    print(age, bmi, risk, '\n')
    do_again = input('Would you like to continue with another risk level? (y or n): ')
