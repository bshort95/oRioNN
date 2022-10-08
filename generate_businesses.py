import random

def generate_businesses(quantity):
    '''Returns a list with the given quantity of business names.'''
    businesses = []
    for n in range(1, quantity + 1):
        # Chance to use a last name as an adjective instead
        random_number = random.randint(1, 4)
        if random_number > 1:
            source_file = 'data/business_adjectives.txt'
        else:
            source_file = 'data/last_names.txt'

        # Get first and second parts
        with open(source_file) as file:
            adjectives = file.readlines()
            adjective = adjectives[random.randint(1, (len(adjectives) - 1))].strip()

        with open('data/business_verbs.txt') as file:
            verbs = file.readlines()
            verb = verbs[random.randint(1, (len(verbs) - 1))].strip()

        business = adjective + " " + verb
        businesses.append(business)
    
    return businesses


# Testing
# businesses = generate_businesses(5)
# print(businesses)