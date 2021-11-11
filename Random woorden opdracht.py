import random

def randomw(Word):
    Scrambled = ''.join(random.sample(Word, len(Word)))
    print("")
    print(Scrambled)

input1 = input("Voer een woord in ")
input2 = input("Voer een 2e woord in ")
input3 = input("Voer een 3e woord in ")
print("")

randomw(input1)
randomw(input2)
randomw(input3)