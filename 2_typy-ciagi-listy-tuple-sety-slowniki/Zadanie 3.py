def mnoznaMnoznik (mnozna, mnoznik):
    if mnozna == 0 or mnoznik == 0:
        wynik = 0
    else:
        wynik = mnozna * mnoznik

    return wynik

a = int(input("Wprowadź mnożną : "))
b = int(input("Wprowadź mnożnik : "))

ab = mnoznaMnoznik(a,b)

if ab == 0:
    print("Mnożna i mnożnik nie mogą być równe 0")
else:
    print("Wynik to : ",ab)