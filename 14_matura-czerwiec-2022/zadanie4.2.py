import math

plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

liczby = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    liczby.append(wiersz)

max_roznica = 0
max_liczba = 0

for liczba in liczby:
    odbicie = int(liczba[::-1])
    liczby_roznica = int(liczba) - odbicie
    if math.fabs(liczby_roznica)>max_roznica:
        max_roznica = int(math.fabs(liczby_roznica))
        max_liczba = liczba

plik.close()

plik = open('wyniki4.txt', 'a')

plik.write(f'\n\n4.2:\n\n{max_liczba} {max_roznica}')

plik.close()