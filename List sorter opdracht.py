
stringlijst = []
integerlijstlijst = []
booleanslijstlijst = []
floatlijst = []

lijst = ['a', "Goodbye", 12.6,15.9,18, True, False, "Yannick"] 

for stringlist in lijst:
    if(type(stringlist) == str):
        stringlijst = stringlist
        print(stringlijst)
print("")

for floatlist in lijst:
    if(type(floatlist) == float):
        floatlijst = floatlist
        print(floatlijst)
print("")

for intlist in lijst:
    if(type(intlist) == int):
        integerlijsts = intlist
        print(integerlijsts)
print("")

for boollist in lijst:
    if(type(boollist) == bool):
        booleanslijst = boollist
        print(booleanslijst)