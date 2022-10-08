run = True
i = True
j = True
while run == True:

    while i == True:
        pos = int(input("How many positive surveys would you like generated: "))
        if pos < 1:
            print("Enter a valid amount: ")
        else:
            i = False
    while j == True:
        neg = int(input("How many negative surveys would you like generated: "))
        if neg < 1:
            print("Enter a valid amount: ")
        else:
            j = False
    n = pos + neg
    nameList = nameGenerator(n)
    compList = companyGenerator(n)
    numList = numGenerator(n)
    surveyList = models(pos, neg)


