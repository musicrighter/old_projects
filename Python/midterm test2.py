def num(x, y):
    if x >= y:
        return 0
    else:
        return num(x+1, y)

print(num(2, 5))
    
