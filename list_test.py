available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# print(available_toppings)

requested_toppings = input('Enter your toppings: ').split(', ')

for toping in requested_toppings:
    if toping in available_toppings:
        print(f'Adding {toping.title()}')
        print('Finished making your pizza!')


    elif toping != available_toppings:
        print('Are you sure you want a plain pizza? (y,n)')
        if input() == 'y':
            print('Making your pizza without that topping.')
            print('Finished making your pizza!')
        else:
            print('Please choose from the available toppings next time.')
        



