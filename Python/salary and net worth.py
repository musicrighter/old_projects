big_salary_limit = 100000
big_net_worth = 500000
salary = float(input('Approx salary: '))
past_donations = input('Type y if donated in the past: ')
net_worth = float(input('Approx net worth: '))

big_salary = salary >= big_salary_limit
big_net_worth = net_worth >= big_net_worth
prior_donations = past_donations == 'y'

if big_salary and big_net_worth:
    category = 'Group 1'

elif big_net_worth and prior_donations:
    category = 'Group 2'

elif big_salary and prior_donations:
    category = 'Group 3'

else:
    category = 'Group 4'

print(category)
