# David Gustafson  Lab-9

def read_names(file_name):
    with open(file_name, 'r') as my_file:
        name_list = []
        for line in my_file:
            line = line.strip()
            line_list = line.split(',')
            name = line_list[0]
            name = name.lower()
            line_list[0] = name
            sex = line_list[1]
            count = int(line_list[2])
            line_list[2] = count
            name_list.append(line_list)
    return name_list

def search(big_list, who):
    result_list = []
    for i in range(len(big_list)):
        student_list = big_list[i]
        name = student_list[0]
        if name == who:
            result_list.append(i)
    return result_list

def display_results(name_list, result_list):
    print('SEARCH RESULTS:\n')
    Name = fixed_width('Name:', 16, ' ')
    Gender = fixed_width('Sex:', 7, ' ')
    print(Name, Gender, 'Count:')
    name_count = 0
    all_names = 0
    for i in result_list:
        line = name_list[i]
        name = line[0]
        name = name.capitalize()
        name = fixed_width(name, 16, ' ')
        sex = line[1]
        sex = fixed_width(sex, 7, ' ')
        count = int(line[2])
        print(name, sex, count)
        name_count += 1
        all_names += count
    print('-' * 32)
    if name_count > 0:
        print('There were', all_names, 'total people')
        print('with', name_count, 'total name(s)')
    elif name_count == 0:
        print('There are no names in the file')

def fixed_width(item, width, pad_char):
    n = len(item)
    pad_len = width - n
    fixed_width_item = item + (pad_len * pad_char)
    return fixed_width_item

name_list = read_names("yob1996.txt")

print(' ' + '_' * 49)
print('|' + ' '*11 + "US Baby name data from 1996" + ' '*11 + '|')
print('|' + ' '*5 + '26,419 records read from baby name file' + ' '*5 + '|')
print('|' + '_' * 49 + '|')

more = 'y'
while more == 'y':
    print('\nNUMBER    SEARCH TYPE:')
    print(''' (1)      'Whole name in list'
 (2)      'Starts with letters in name' 
 (3)      'Ends with letters in name' 
 (4)      'Contains letters in name'
 (5)      'Most popular female name(s)'
 (6)      'Most popular male name(s)'\n''')
    what = input('Type of search?: ')

    if what == '1':
        who = input('What is the full name?: ')
        who = who.lower()
        result_list = search(name_list, who)
        display_results(name_list, result_list)

    elif what == '2':
        who = input('What does the name start with?: ')
        who = who.lower()
        result_list = []
        for i in range(len(name_list)):
            aname = name_list[i]
            name = aname[0]
            if name.startswith(who):
                result_list.append(i)
        display_results(name_list, result_list)
        
    elif what == '3':
        who = input('What does the name end with?: ')
        who = who.lower()
        result_list = []
        for i in range(len(name_list)):
            aname = name_list[i]
            name = aname[0]
            if name.endswith(who):
                result_list.append(i)
        display_results(name_list, result_list)
                
    elif what == '4':
        who = input('What letters does the name contain?: ')
        who = who.lower()
        result_list = []
        for i in range(len(name_list)):
            aname = name_list[i]
            name = aname[0]
            if who in name:
                result_list.append(i)
        display_results(name_list, result_list)

    elif what == '5':
        result_list = []
        number = int(input('How many names?: '))
        for i in range(len(name_list)):
            line = name_list[i]
            sex = line[1]
            if sex == 'F':
                for i in range(number):
                    result_list.append(i)
            break
        display_results(name_list, result_list)

    elif what == '6':
        result_list = []
        number = int(input('How many names?: '))
        for i in range(len(name_list)):
            line = name_list[i]
            sex = line[1]
            if sex == 'F':
                for i in range(number):
                    result_list.append(15887 + i)
            break
        display_results(name_list, result_list)
        
    more = input('\nSearch again? Press y or n: ')
    more = more.lower()[0]
