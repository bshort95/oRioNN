import random

def generate_reviews(number,sen):
    
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
        total_list.append(temp_list[random.randint(0, (len(temp_list) -1))])
    
    
    return total_list
