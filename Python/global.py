x = 2

def a():
    global x
    x = x * 6

def b():
    global x
    x = x // 3

def c():
    global x
    x = x + 6

def d():
    global x
    x = x % 7

print(x)
a()
print(x)
b()
print(x)
c()
print(x)
d()
print(x)
