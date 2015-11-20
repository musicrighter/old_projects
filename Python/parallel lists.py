names = ['Ann', 'Fred', 'Brianna', 'Kyle', 'Fred', 'Red']

heights = [61, 70, 64, 72, 48, 68]

def fixed_width(item, width, pad_char):
    n = len(item)
    pad_len = width - n
    fixed_width_item = item + (pad_len * pad_char)
    return fixed_width_item

def show_contents():
    print('Contents of lists:')
    name = fixed_width('Name:', 20, '.')
    print('  # Name:' + '             Height:')
    for i in range(len(names)):
        i_show = format(i + 1, '3d')
        print(i_show, fixed_width(names[i], 20, '.'), str(heights[i]) + 'in')
    print()

show_contents()

# Standardize names as lower case
for i in range(len(names)):
    names[i] = names[i].lower()

# Whole name in list
who = 'Fred'
who = who.lower()
print("'Whole name in list'")
for i in range(len(names)):
    aname = names[i]
    if who == aname:
        print('Found', who, heights[i], names[i])
print()

# Starts with letters in list
who = 'F'
who = who.lower()
print("'Starts with letters in list'")
for i in range(len(names)):
    aname = names[i]
    if aname.startswith(who):
        print('Found', who, heights[i], names[i])
print()

# Starts with letters in list
who = 'F'
who = who.lower()
print("'Starts with letters in list'")
for i in range(len(names)):
    aname = names[i]
    n = len(who)
    if who == aname[:n]:
        print('Found', who, heights[i], names[i])
print()

# Ends with letters in list
who = 'red'
who = who.lower()
print("'Ends with letters in list'")
for i in range(len(names)):
    aname = names[i]
    if aname.endswith(who):
        print('Found', who, heights[i], names[i])
print()

# Contains letters in list
who = 'Nn'
who = who.lower()
print("'Contains letters in list'")
for i in range(len(names)):
    aname = names[i]
    if who in aname:
        print('Found', who, heights[i], names[i])
print()

# Contains letters in list
who = 'Nn'
who = who.lower()
show_who = who.capitalize()
print("'Contains letters in list'")
for i in range(len(names)):
    aname = names[i]
    if who in aname:
        show_name = aname.capitalize()
        print('Found', show_who, heights[i], show_name)
print()





        
