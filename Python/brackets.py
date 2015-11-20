def fixed_width(thing, width):
    n = len(thing)
    nblanks = width - n
    nice_thing = thing + nblanks * '.'
    return nice_thing

products = ['bus', 'car', 'go cart', 'jet']

prices = [4.50, 21.95, 16.40, 11.97]

# find longest item in products
longest = -999
for item in products:
    n = len(item)
    if n > longest:
        longest = n

# find most expensive item in prices
highest = 0
for item in prices:
    if item > highest:
        highest = item

print('Most expensive item is $' + str(highest))
print('Longest item is', longest, 'characters \n')

width = longest + 4
for i in range(len(products)):
    item = products[i] + ':'
    price = '$' + str(prices[i])
    print(fixed_width(item, width), price)
    
