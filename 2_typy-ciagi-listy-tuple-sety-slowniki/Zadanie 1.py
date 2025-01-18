imiona = ["Adam","Wojtek","Bartek","Marek","Łucja","Magda","Ela","Maja"]

meskie = input("Wprowadź imię męskie : ")
zenskie = input("Wprowadź imię żeńskie : ")

for i in imiona :
    print(i)
else :
    if meskie in imiona :
        print("imie ",meskie," znajduje się w liście")
    else :
        print("imie ",meskie, " NIE znajduje się w liście")

    if zenskie in imiona :
        print("imie ",zenskie, " znajduje się w liście")
    else :
        print("imie ",zenskie, " NIE znajduje się w liście")
