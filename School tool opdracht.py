weekdag = False

print("Wat voor dag is het? Kies uit: maandag / dinsdag / woensdag / donderdag / vrijdag / zaterdag / zondag")
daginput = input("Welke dag is het: ")
if daginput != ("zaterdag") or daginput != ("zondag"):
    week = True
    print("Het is bijna weekend.")
elif daginput == ("zaterdag") or daginput == ("zondag"):
    weekend = True
    print("Het is weekend.")

if week:
    schooldag = True
elif weekend:
    schooldag = False

if schooldag == True:
  print("Sta op en ga naar school.")
else:
  print("Gaming tijd")