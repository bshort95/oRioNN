from functions.csv_writer import csv_writer
from functions.generate_businesses import generate_businesses
from functions.generate_names import generate_names
from functions.generate_numbers import generate_numbers
from functions.model_generator import generate_reviews

# Get the number of positive survey responses to generate
valid_input = False
while valid_input == False:
    num_positives = int(input("How many positive surveys would you like to generate?: "))
    if num_positives >= 0:
        valid_input = True
    else:
        print("Please enter a whole number of 0 or more.")
    
# Get the number of negative survey responses to generate
valid_input = False
while valid_input == False:
    num_negatives = int(input("How many negative surveys would you like to generate?: "))
    if num_negatives >= 0:
       valid_input = True
    else:
        print("Please enter a whole number of 0 or more.")

numbers_list = []
names_list = []
business_list = []
sentences_list = []

if num_positives > 0:
    numbers_list.append(generate_numbers(True, num_positives))
    names_list.append(generate_names(num_positives))
    business_list.append(generate_businesses(num_positives))
    sentences_list.append(generate_reviews(num_positives, "p")) 

if num_negatives > 0:
    numbers_list.append(generate_numbers(True, num_negatives))
    names_list.append(generate_names(num_negatives))
    business_list.append(generate_businesses(num_negatives))
    sentences_list.append(generate_reviews(num_negatives, "n"))

full_list = [names_list, business_list, numbers_list, sentences_list]
csv_writer(full_list)