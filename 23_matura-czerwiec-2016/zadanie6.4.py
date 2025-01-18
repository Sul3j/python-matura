plik = open("liczby.txt", "r")
wiersze = plik.readlines()

tab = []
wynik = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    tab.append([int(wiersz[:-1]), int(wiersz[-1])])

for i in tab:
    if i[1] == 8:
        wynik += int(str(i[0]), 8)

plik.close()
plik = open("wynik_6_4.txt", "w")
plik.write(f"{wynik}\n")
plik.close()