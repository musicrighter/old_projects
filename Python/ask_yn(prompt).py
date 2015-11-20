def ask_yn(prompt):
    answer = input(prompt + ' ')
    answer = answer.lower()
    answer = answer [0]
    if answer in 'yn':
        return answer
    else:
        return ask_yn(prompt)

again = 'y'
while again == 'y':
    more = ask_yn('Do some more? Press y or n')
    print('You replied', more)
    again = more
