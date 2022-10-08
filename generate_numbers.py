import random

def generate_numbers(is_positive):
    '''Generates numerical scores for each field. First, the individual scores
    will be generated, then determines the averages.

    Parameter: True for positive scores, False for negative scores.
    
    Output: Returns a list with every field, at the following indices:
    * 0 - Average Rating
    * 1 - Outcome Average Score
    * 2 - Caregiver's Average Score
    * 3 - Office Staff Average Score
    * 4 - Likely to recommend
    * 5 - Impact of service
    * 6 - Caregiver ability
    * 7 - Communication and helpfulness
    * 8 - Needs and preferences
    '''

    assert is_positive == True or is_positive == False
    
    # Outcomes
    likely_to_recommend = random.randint(1, 5)
    impact_of_service = random.randint(1, 5)
    caregiver_ability = random.randint(1, 5)

    # Office Staff Satisfaction
    communication_and_helpfulness = random.randint(1, 5)
    matched_needs = random.randint(1, 5)

    if is_positive:
        likely_to_recommend += 5
        impact_of_service += 5
        caregiver_ability += 5
        communication_and_helpfulness += 5
        matched_needs += 5
    
    outcome_average = (likely_to_recommend + impact_of_service) / 2
    caregiver_average = caregiver_ability
    
    office_staff_average = (communication_and_helpfulness + matched_needs) / 2

    average_rating = (likely_to_recommend + impact_of_service + caregiver_ability
    + communication_and_helpfulness + matched_needs) / 5

    scores = [average_rating, outcome_average, caregiver_average,
    office_staff_average, likely_to_recommend, impact_of_service,
    caregiver_ability, communication_and_helpfulness, matched_needs]

    return scores
    

def print_scores(scores):
    '''Prints the result of each field for testing purposes
    
    Parameter: Enter the output of the generate_numbers() function.
    '''
    print(f"Average Rating: {scores[0]}")
    print(f"Outcome Average Score: {scores[1]}")
    print(f"Caregiver's Average Score: {scores[2]}")
    print(f"Office Staff Average Score: {scores[3]}")

    print(f"Likely to recommend: {scores[4]}")
    print(f"Impact of service: {scores[5]}")
    print(f"Caregiver ability: {scores[6]}")
    print(f"Communication and helpfulness: {scores[7]}")
    print(f"Needs and preferences: {scores[8]}")


# Testing
# scores = generate_numbers(True)
print_scores(scores)