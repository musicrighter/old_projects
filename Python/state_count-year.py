import time

more = 'y'
while more == 'y':
    who = input('Type first name to look for: ').lower().strip()
    start_search_time = time.time()
    results = []
    for little_list in names_list:
        if little_list[3] == who:
            results.append(little_list)

    end_search_time = time.time()
    search_time = end_search_time - start_search_time
    show_search_seconds = format(search_time, '9,.4f')
    print('Search time', show_search_seconds, 'seconds')
    print()

    current_state = ''
    state_count = 0
    state_year = 0
    for little_list in results:
        state = little_list[0]
        count = little_list[4]
        year = little_list[2]
        if state != current_state:
            #print(state, ' New state detected')
            if state_count > 0
                print(current_state, state_count, state_year)
            current_state = state
            state_count = count
            state_year = year
        elif count > state_count:
            state_count = count
            state_year = year

    more = input('Look again? Press y or n: ').lower()

samples = 0






    



















            
