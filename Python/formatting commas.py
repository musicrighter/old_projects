def int_commas(number):
    ''' (int) -> str
        1234567 -> '1,234,567'
    '''
    return format(number, ',d')

population = 3000000000
pop_display = int_commas(population)
print(pop_display)


def float_to_money(value):
    ''' (float) -> str
        4.3 4.30
    ''' 
    return format(value, ',.2f')

amount = 501
money = float_to_money(amount)
print(money)

