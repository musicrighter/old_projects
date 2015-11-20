def add_one(my_list):
    for i in range(len(my_list)):
        my_list[i] = my_list[i] + 1
    return

def list_largest(my_list):
    largest = my_list[0]
    for number in my_list:
        if number > largest:
            largest = number
    return largest

def list_average(my_list):
    total = 0
    for number in my_list:
        total += number
    ave = total / len(my_list)
    return ave

numbers = [55, 78.2, 99, 1001, -65]
numbers1 = [55, 78.2, 99, 1001, -65]
numbers2 = [55, 78.2, 99, 1001, -65]

print('numbers, before calling add_one(numbers)')
print(numbers, '\n')

add_one(numbers1)

print('numbers, after calling add_one(numbers)')
print(numbers1, '\n')

for i in range(len(numbers)):
    numbers2[i] = numbers2[i] ** 2

print('numbers, after squaring')
print(numbers2)

x = list_largest(numbers)
print('\nlargest number in list:', x)

y = list_largest(numbers1)
print('\nlargest number in list after adding 1:', y)

z = list_largest(numbers2)
print('\nlargest number in list after squaring:', z)

w = list_average(numbers)
print('\naverage is:', round(w, 2))

v = sum(numbers)
print('\nsum of numbers is: ', v)
