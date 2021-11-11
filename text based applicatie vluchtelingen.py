print("Het jaar is 2019 en de Taliban valt aan in de noordelijke Balkh provincie. In het Herat district word veel gevochten, Ik wil naar het vliegveld toe zien te komen maar ik heb geen vorm van transportatie en moet dus iets regelen. ")

print("Wat moet ik doen?")
answer1 = input("(A)  Ik bel familie op en vraag of iemand mij erheen kan brengen. (B)  Ik probeer iemand te vinden op straat die mij er naar toe wil brengen.")
print("")
if answer1 == "A" or answer1 == "a":
    print("Ik bel familie leden op en uiteindelijk wil mijn broer mij naar het vliegveld brengen. ")
    answer2 = input("Mijn broer komt mij ophalen en vraagt aan mij waarom ik naar het vliegveld wil, wat vertel ik hem? (A) De waarheid. (B) Dat ik op vakantie ga. ")
    print("")
    if answer2 == "A" or answer2 == "a":
        print("Ik vertel hem dat ik wil proberen te vluchten en vraag hem om mee te gaan. ")
        print("Mijn broer verteld mij dat hij niet mee kan omdat hij een gezin heeft en voor hun moet zorgen, ik ben bang dat hij het niet overleeft als hij niet met zijn gezin vlucht.")
        print("Ik ga naar het vliegtuig toe en stap in, ik mis mijn broer maar weet dat ik nu veilig in Nederland kan leven.")
    elif answer2 == "B" or answer1 == "b":
        print("Hij zegt dat hij het leuk vind voor mij en dat ik er van moet genieten!")
        answer4 = input("Ik koop een vliegticket en wacht op het vliegtuig, iemand vraagt aan mij waarom ik zo snel weg wil, wat moet ik zeggen? (A). Ik zeg dat ik op vakantie ga (B). Ik zeg dat ik snel weg wil vanwege het conflict. ")
        if answer4 == "A" or answer4 == "a":
            print("Hij geloofd mij niet en word boos, gelukkig is mijn vlucht er en kan ik weg. Ik ga zitten in het vliegtuig en ik ga onderweg naar Nederland. ")
            print("Ik kom veilig aan en wordt opgevangen, Ik ben nu eindelijk veilig.")
        elif answer4 == "B" or answer4 == "b":
            print("Hij zegt dat ik er bang uit zie maar gelooft mij vanwege dat er buiten conflicten zijn, ik vlucht en kom veilig aan in Nederland. ")
            print("Ik ben aangekomen en word opgevangen in een centrum. Ik ben veilig")


elif answer1 == "B" or answer1 == "b":
    print("Iemand op straat zegt dat zij mij wel naar het vliegveld wil brengen, ik vertrouw het niet helemaal.")
    print("De persoon vraagt aan mij waarom ik naar het vliegveld ga.")
    answer3 = input("(A) Ik zeg dat ik op vakantie ga. (B) Ik zeg dat ik ga vluchten ")
    if answer3 == "A" or answer3 == "a":
        print("De persoon verteld mij dat hij weet dat ik ga vluchten en wil mee, ik zeg tegen hem dat dat kan. We gaan naar het vliegveld toe. ")
        answer6 = input("Ik koop een vliegticket en wacht op het vliegtuig met de man, er komt iemand op ons af en zegt dat hij weet dat we gaan vluchten, wat moet ik zeggen? (A). Dat wij niet gaan vluchten. (B). Dat wij wel gaan vluchten. ")
    elif answer3 == "B" or answer3 == "b":
        print("Hij zegt dat hij mee wil vluchten en rijd naar het vliegveld toe.")
        answer5 = input("Ik koop een vliegticket en wacht op het vliegtuig met de man, er komt iemand op ons af en zegt dat hij weet dat we gaan vluchten, wat moet ik zeggen? (A). Dat wij niet gaan vluchten. (B). Dat wij wel gaan vluchten. ")
        if answer5 == "A" or answer5 == "a":
            print("De man wordt boos en begint te schreeuwen, hij wordt het vliegveld uitgezet en het vliegtuig is er.")
            print("Ik en de man vluchten naar Nederland en komen veilig aan.")
            print("Wij zijn aangekomen en worden opgevangen in een centrum. Ik ben veilig.")
        elif answer5 == "B" or answer5 == "b":
            print("De man wordt boos en begint te schreeuwen, hij wordt het vliegveld uitgezet en het vliegtuig is er.")
            print("Ik en de man vluchten naar Nederland en komen veilig aan.")
            print("Wij zijn aangekomen en worden opgevangen in een centrum. Ik ben veilig.")
