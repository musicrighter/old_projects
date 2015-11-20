# David Gustafson Lab 8

print("ShopMart's exclusive Thanksgiving specials:")

def fixed_width(item, width, pad_char):
    n = len(item)
    pad_len = width - n
    fixed_width_item = item + (pad_len * pad_char)
    return fixed_width_item

def display_products(products, prices):
    print("\nShopMart's Thanksgiving Specials:")
    desc = fixed_width('Description', 16, '.')
    print('  # ' + str(desc) + '      Price')
    for i in range(len(products)):
        i_show = format(i + 1, '3d')
        price_show = format(prices[i], '10,.2f')
        print(i_show, fixed_width(products[i], 16, '.'), price_show)
    print()

def display_cart_qty(cartQty, products, prices):
    print("\nShopping cart contents:")
    desc = fixed_width('Qty Item', 20, '.')
    print(str(desc) + '      Price   Subtotal')
    for i in range(len(products)):
        if cartQty[i] > 0:      
            i_show = format(cartQty[i], "3d")
            price_show = format(prices[i], "10,.2f")
            subtotal_show = format((cartQty[i]*prices[i]), '10.2f')
            print (i_show, fixed_width(products[i], 16,'.'), price_show, subtotal_show)
    print('Your cart total is:           $     ', format(total_owed, ',.2f'))
    print ("_" * 48)
    
products  = ['Turkey', 'Cranberry', 'Pumpkin Pie', 'Spicy Latte', 'Yams']
prices    = [   26.95,        3.95,          8.95,          4.95,   1.99]
cartQty   = [       0,           0,             0,             0,      0]

total_owed = 0.00

action = input("\nAction: Shop('s'), Checkout('c'), Cancel('x')?: ")

while action == "s":
    display_products(products, prices)
    choice = input('Product number: ')
    p = int(choice) -1
    item = products[p]                
    price = prices[p]
    print('You added', item, price, 'to your shopping cart')
    total_owed = total_owed + price
    cartQty[p] = cartQty[p] + 1
    display_cart_qty(cartQty, products, prices)
    action = input("\nAction: Shop('s'), Checkout('c'), Cancel('x')?: ")

if action == 'c' and total_owed > 0:
    print("\nChecking out, please pay for your shopping cart contents:")
    print('Please pay $' + str(format(total_owed, ',.2f')))
    print('\nThank you for shopping at ShopMart')
elif action == 'c':
    print("\nYou didn't purchase anything so you owe us nothing.")
    print("Thanks for visiting ShopMart")
elif action == 'x':
    print("\nThanks for visiting ShopMart")
    total_owed = 0.00
    print('You cancelled your order, so you owe us nothing.')

print('Finished')
