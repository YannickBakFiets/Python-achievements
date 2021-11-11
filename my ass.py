myList = [5, 5, 3, 1]

lowest_number = 100000000;
for eachNumber in myList:
    print(eachNumber)
    if eachNumber < lowest_number:
        lowest_number = eachNumber
print("lowestnumber: ", lowest_number)