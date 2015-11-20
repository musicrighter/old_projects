ph = input('Please enter a phone number: ')

dig_val = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def ph_int(ph):
    li = []
    for ch in ph:
        if ch in '0123456789':
            temp = dig_val[ch]
            li.append(temp)
    ''.join(li)
    return li
            

print(ph_int(ph))
            
