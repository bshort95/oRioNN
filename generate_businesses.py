import random

def generate_businesses(quantity):
    '''Returns a list with the given quantity of business names.'''
    businesses = []
    # Open each file and store a list of each one
    with open('data/business_adjectives.txt') as file:
        adjectives = file.readlines()
    with open('data/last_names.txt') as file:
        last_names = file.readlines()
    with open('data/business_verbs.txt') as file:
        verbs = file.readlines()

    for n in range(1, quantity + 1):
        # Get first part, with a chance to use a last name as an adjective instead
        random_number = random.randint(1, 4)
        if random_number > 1:
            adjective = adjectives[random.randint(1, (len(adjectives) - 1))].strip()
        else:
            adjective = last_names[random.randint(1, (len(adjectives) - 1))].strip()

        # Get second part
        verb = verbs[random.randint(1, (len(verbs) - 1))].strip()
        # Put the parts together and append to list
        business = adjective + " " + verb
        businesses.append(business)
    
    return businesses


# Testing
businesses = generate_businesses(10)
print(businesses)