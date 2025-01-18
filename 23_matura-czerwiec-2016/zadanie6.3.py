plik = open("liczby.txt", "r")
wiersze = plik.readlines()

tab = []
wynik = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    tab.append([int(wiersz[:-1]), int(wiersz[-1])])

for i in tab:
    if i[1] == 2 and int(str(i[0]), 2) % 2 == 0:
        wynik += 1

plik.close()
plik = open("wynik_6_3.txt", "w")
plik.write(f"{wynik}\n")
plik.close()