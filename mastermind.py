from doctest import master
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
consent_list = []

if num_positives > 0:
    numbers_list.append(generate_numbers(True, num_positives))
    names_list.append(generate_names(num_positives))
    business_list.append(generate_businesses(num_positives))
    sentences_list.append(generate_reviews(num_positives, "p")) 
    for n in range(1, (num_positives + 1)):
        consent_list.append("Yes")

if num_negatives > 0:
    numbers_list.append(generate_numbers(True, num_negatives))
    names_list.append(generate_names(num_negatives))
    business_list.append(generate_businesses(num_negatives))
    sentences_list.append(generate_reviews(num_negatives, "n"))
    for n in range(1, (num_negatives + 1)):
        consent_list.append("No")

temp_list = numbers_list[0]
for w in numbers_list[1]:
    temp_list.append(w)
numbers_list = temp_list



temp_list = names_list[0]
for w in names_list[1]:
    temp_list.append(w)
names_list = temp_list


temp_list = business_list[0]
for w in business_list[1]:
    temp_list.append(w)
business_list = temp_list




comment_list = sentences_list[0]
for w in sentences_list[1]:
    comment_list.append(w)
sentences_list = comment_list






master_list = []
full_list = [names_list, business_list, numbers_list, sentences_list, consent_list]


for i in range(len(names_list)):
    
    master_list.append([names_list[i], business_list[i],"Active Client",numbers_list[i][0], numbers_list[i][1], numbers_list[i][2],
    numbers_list[i][3], sentences_list[i][0],numbers_list[i][4],
    sentences_list[i][1], numbers_list[i][5],
    sentences_list[i][2], numbers_list[i][6],
    sentences_list[i][3], numbers_list[i][7],
    sentences_list[i][4], numbers_list[i][8],
    sentences_list[i][5], consent_list[i]])

csv_writer(master_list)