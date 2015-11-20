things = []
again = 'y'
while again == 'y':
    item = input('Type an item ')
    things.append(item)
    again = input('Again? Press y or n ')
    
print()
print(things)
things[1] = 99.775
print(things)

ideas = []   # empty list Note use of square brackets
scores = [40, 39, 37, 10, 48]
# items numbered starting at 0, think 'offset from start'
x = scores[0]   # 40
y = scores[2]   # 37
n_items = len(scores)   # 5 items right now
z = scores[len(scores) -1]   # last item 48
z2 = scores[-1]   # last item 48a

for item in scores:
    print(item)
    if item >= 40:
        print('Way to go!')

# add up all the scores
score_sum = 0
for item in scores:
    score_sum += item
    print(item, score_sum)

# this means the same as the previous loop
score_sum = 0
for i in range(len(scores)):
    item = scores[i]
    score_sum += item
    print(item, score_sum)

# another way
score_sum2 = sum(scores)



