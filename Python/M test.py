# who = input("What's your name? ").capitalize()
weight = float(input("What's your weight? "))
height = float(input("What's your height in inches? "))

bmi = (weight / (height * height)) * 703

if bmi <= 18.5:
    cat = 'Underweight'
elif bmi < 25:
    cat = 'Normal weight'
elif bmi < 30:
    cat = 'Overweight'
elif bmi >= 30:
    cat = 'Obesity'

print('Your BMI is', round(bmi, 1))
print('You are classified under', cat)


'''
print()
print('Your name is', str(who) + ', your weight is', str(weight), 'pounds,')
print('and your height is', height[0], 'feet', height[2:], 'inches')
'''


