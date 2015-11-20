employees = [['Ann', 61, 25],
             ['Fred', 70, 5],
             ['Brianna', 64, 14],
             ['Kyle', 72, 16],
             ['Fred', 48, 60],
             ['Red', 68, 4]]

# Standardize the list of little lists
for i in range(len(employees)):
    employees[i][0] = employees[i][0].lower()

who = 'RED'
who = who.lower()

# Display the list of little lists
for sublist in employees:
    name = sublist[0]
    height = sublist[1]
    bonus = sublist[2]
    if name.endswith(who):
        print(name.capitalize(), height, bonus)
