from csv_writer import csv_writer
from generate_businesses import generate_businesses
from generate_names import generate_names
from generate_numbers import generate_numbers

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

if num_positives > 0:
    names_list = generate_names(num_positives)
    business_list = generate_businesses(num_positives)
    numbers_list = generate_numbers(True)
    #sentences_list = model_generator(num_positives)       <---- do this

if num_negatives > 0:
    names_list.append(generate_names(num_negatives))
    business_list.append(generate_businesses(num_negatives))
    numbers_list.append(generate_numbers(True))
    #sentences_list = model_generator(num_positives)       <---- do this

full_list = [names_list, business_list, numbers_list]
csv_writer(full_list)