import random

def generate_reviews(p,n):
    
    total_list = []
    p_list = []
    n_list = []
    
    for x in open("good.txt"):
        p_list.append(x)
    for y in open("bad.txt"):
        n_list.append(y)
    
   
    for i in range(p):
        total_list.append(n_list[random.randint(0,p)])
    
    for j in range(n):
        total_list.append(n_list[random.randint(0,n)])

    return total_list

print(generate_reviews(1,2))
