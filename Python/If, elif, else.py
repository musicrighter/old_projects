amt = 1654

if amt < 100 and amt > 0:
    group = 'OK'
elif amt <= 500:
    group = 'Bronze'
elif amt <= 1000:
    group = 'Silver'
elif amt > 1000:
    group = 'Gold'
    print('We are naming Oregon Hall for you')
else:
    group = 'Gold'
print(group)
