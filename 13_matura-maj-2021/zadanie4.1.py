plik = open("przyklad.txt", "r")
wiersze = plik.readlines()

instrukcje = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    instrukcje.append(wiersz.split(" "))

slowo = []
print(instrukcje)
for instrukcja in instrukcje:
    if instrukcja[0] == "DOPISZ":
        slowo.append(instrukcja[1])
    elif instrukcja[0] == "ZMIEN":
        slowo.pop()
        slowo.append(instrukcja[1])
    elif instrukcja[0] == "USUN":
        slowo.pop()
    elif instrukcja[0] == "PRZESUN":
        if instrukcja[1] in slowo:
            indeks = slowo.index(instrukcja[1])
            # ord() zamienia literę na kod ascii
            if ord(slowo[indeks]) == 90:
                slowo[indeks] = "A"
            else:
                slowo[indeks] = chr(ord(slowo[indeks])+1)

plik.close()

plik = open("rozwiazanie.txt", "w")
plik.write("4.1: \n")
plik.write(str(len(slowo)))

plik.close()
