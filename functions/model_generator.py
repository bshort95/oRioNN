from doctest import master
import random

def generate_reviews(number,sen):
    master_list= []
    total_list = []
    temp_list = []
    data = ""
    if sen == "p":
        data = r"data\good.txt"
    else:
        data = r"data\bad.txt"
    
    for y in open(data):
        temp_list.append(y)
    
    for i in range(number):
        for j in range(5):
            total_list.append(temp_list[random.randint(0, (len(temp_list) -1))])
        master_list.append(total_list)
    
    return master_list
