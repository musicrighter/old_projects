def get_students(file_name):
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
        print('DEBUG', student_list)
        if name == who:
            result_list.append(-1)
    return result_list

def display_results(class_list, result_list):
    for i in result_list:
        student = class_list[i]
        #stub
        print(student)


class_list = get_students('students.txt')

print('DEBUG', class_list)

more = 'y'
while more == 'y':
    what = input('Type of search: S (student name), Y (year), M (major)')

    if what.upper()[0] == 'S':
        who = input('Type first name to look for: ')
        result_list = search(class_list, who)

    elif what.upper()[0] == 'Y':
        year = input('Type year to look for: ')
        result_list = search(class_list, year)
    
    elif what.upper()[0] == 'M':
        major = input('Type major to look for: ')
        result_list = search(class_list, major)

    more = input('Search again? Press y or n: ')
    more = more.lower()[0]

print('Finished')

        
