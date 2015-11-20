# David Gustafson

def get_float():
    '''Gets a number and multipies it by 2,
       then rounds it to two decimal places
       and prints it.
    '''
    price = float(input('Please enter the price: '))
    price = price * 2
    price = round(price, 2)
    print(price)

get_float()
