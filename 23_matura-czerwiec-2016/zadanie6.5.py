plik = open("liczby.txt", "r")
wiersze = plik.readlines()

tab = []
wynik = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    tab.append([int(wiersz[:-1]), int(wiersz[-1])])

kod_min = wiersze[0].strip()
kod_max = wiersze[0].strip()
wartosc_min=int(str(tab[0][0]),tab[0][1])
wartosc_max=int(str(tab[0][0]),tab[0][1])

for i in tab:
    if wartosc_min > int(str(i[0]), i[1]):
        wartosc_min = int(str(i[0]), i[1])
        kod_min = str(i[0]) + str(i[1])
    if wartosc_max < int(str(i[0]), i[1]):
        wartosc_max = int(str(i[0]), i[1])
        kod_max = str(i[0]) + str(i[1])

plik.close()
plik = open("wynik_6_5.txt", "w")
plik.write(f"min wartosc: {wartosc_min} min kod: {kod_min}\n")
plik.write(f"max wartosc: {wartosc_max} max kod: {kod_max}\n")
plik.close()