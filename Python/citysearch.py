map = {}
map['pdx'] = ['sea', 'eug', 'sfo']
map['sea'] = ['van', 'slc', 'lax']
map['slc'] = ['chicago', 'clv']
map['eug'] = ['pdx']
map['sfo'] = ['pdx']
map['chicago'] = ['slc']
map['clv'] = ['slc', 'lax']
map['lax'] = ['sea', 'clv']
map['van'] = ['sea']
map['flo'] = ['min']

def search(start_city, end_city, visited):
    if start_city == end_city:
        return True
    if start_city in visited:
        return False
    visited.append(start_city)
    for city in map[start_city]:
        if search(city, end_city, visited):
            return True
    return False

def main():
    if search('pdx', 'min', []):
        print('connects')
    else:
        print('does not connect')
    

main()
