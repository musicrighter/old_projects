import random

dice = []

for i in range(60000):
    roll = random.randint(1, 6)
    dice.append(roll)

dice_count = [0, 0, 0, 0, 0, 0]

for i in range(len(dice_count)):
    d = dice.count(i+1)
    dice_count[i] = d

for i in range(6):
    print(i + 1, dice_count[i])

'''
for i in range(len(dice)):
    roll = dice[i + 1]
    dice_count[1 - i] = roll
'''

