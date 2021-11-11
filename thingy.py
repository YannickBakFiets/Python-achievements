while True:

    answer1 = input ("Which direction do you want to go? (R for right and L for left) ")
    if answer1 == "r" or answer1 == "R":
        print("You go right and encounter a person")
        print("")
        print("You talk to the person and they give you a free sword. ")
        print("")
        username = input ("Before giving you the sword they ask you for your name: ")
        print("")
        print("Hello there young traveler " + username)
        print("")
        print("You ask the person for their name. They tell you not to worry about it, as you walk away from them you turn around to see they have dissapeard")
        print("")
        answer2 = input("You enter a big room and encounter a monster. What do you do? (F to fight and R to run.) ")
        if answer2 == "f" or answer2 == "F":
                print("")
                print("you fought the monster and after a hard battle you killed it.")
                print("")
                answer5 = input("You find a giant monkey and it speaks to you, do you respond? (T to talk and I to ignore) ")
                if answer5 == "T" or answer5 == "t":
                    print("")
                    print("You talk to the monkey and it gives you banana, you win the game. GG")
                    print("")
                    print("<3 Monkey")
                    print("")
                    username = input("what was your name? ")
                    print("")
                    print("thank you for playing " + username)
                    break
                else:
                    print("You didnt talk to the monkey, the monkey ripped off your head for not being polite. GG ")
                    break

        elif answer2 == "r" or answer2 == "R":
            print("")
            print("You ran and got killed by the monster.")

    elif answer1 == "l" or answer1 == "L":
        print("You go left and encounter a monster")
        answer3 = input("What do you do with the monster? (F to fight and R to run) ")
        if answer3 == "f" or answer3 == "F":
            print("")
            print("You died trying to fight the monster")
        elif answer3 == "r" or answer3 == "R":
            print("")
            print("You run away but the monster chases you.")
            print("")
            answer4 = input ("As you run from the monster you find a place to hide, do you take the chance or do you keep running (H to hide and R to run) ")
            if answer4 == "H" or answer4 == "h":
                print("")
                print("You hid and the monster ran past you.")
                print("")
                print("You run back to where you encountered the monster and are able to traverse through it layer.")
                print("")
                answer6 = input ("You find a giant monkey and it speaks to you, do you respond? (T to talk and I to ignore) ")
                if answer6 == "T" or answer6 == "t":
                    print("")
                    print("You talk to the monkey and it gives you banana, you win the game. GG")
                    print("")
                    print("<3 Monkey")
                    print("")
                    username = input("what was your name? ")
                    print("")
                    print("thank you for playing " + username)
                    break
                else:
                    print("You didnt talk to the monkey, the monkey ripped your head off for not being polite. GG ")
                    print("")
                    username = input("what was your name? ")
                    print("thank you for playing " + username)
                    break

            elif answer4 == "R" or answer4 == "r":
                print("")
                print("You keep running but the monster catches you and eats you.")
                break
            
    else: 
        answer7 = input("Incorrect input. Do you want to try again? (Y to try again N to give up) ")
        if answer7 == "Y" or answer7 == "y":
            continue
        elif answer7 == "N" or answer7 == "n":
            break