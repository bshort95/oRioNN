import random

def generate_names(quantity):
    '''Returns a list with the given quantity of full names.'''
    names = []
    # Open each file and store a list of each one
    with open('data/first_names.txt') as file:
        first_names = file.readlines()
    with open('data/last_names.txt') as file:
        last_names = file.readlines()

    for n in range(1, quantity + 1):
        # Use the lists to get a first and last name
        first_name = first_names[random.randint(1, (len(first_names) - 1))].strip()
        last_name = last_names[random.randint(1, (len(last_names) - 1))].strip()

        # Put the first and last names together and append to list
        full_name = first_name + " " + last_name
        names.append(full_name)
    
    return names
