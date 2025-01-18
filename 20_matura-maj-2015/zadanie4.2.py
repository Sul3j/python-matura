# zależności:
# aby liczba binarna była podzielna przez 2 bez reszty ostatni elementem ciągu musi być 0
# aby liczba binarna była podzielna przez 8 bez reszty ostatnie 3 elementy ciągu muszą być 0

plik = open("liczby.txt", "r")
wiersze = plik.readlines()

podzielne2 = 0
podzielne8 = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz[len(wiersz) - 1] == '0':
        podzielne2 += 1
    if len(wiersz) >= 3:
        if wiersz[-3:].count('0') == 3:
            podzielne8 += 1

plik.close()
plik = open("wyniki4.txt", "a")
plik.write(f"4.2: podzielne przez 2: {podzielne2} podzielne przez 8: {podzielne8}\n\n")
plik.close()
