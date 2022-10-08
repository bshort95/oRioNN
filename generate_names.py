import random

def generate_names(quantity):
    '''Returns a list with the given quantity of full names.'''
    names = []
    for n in range(1, quantity + 1):
        with open('data/first_names.txt') as file:
            first_names = file.readlines()
            first_name = first_names[random.randint(1, (len(first_names) - 1))].strip()

        with open('data/last_names.txt') as file:
            last_names = file.readlines()
            last_name = last_names[random.randint(1, (len(last_names) - 1))].strip()

        full_name = first_name + " " + last_name
        names.append(full_name)
    
    return names


# Testing
# names = generate_names(5)
# print(names)