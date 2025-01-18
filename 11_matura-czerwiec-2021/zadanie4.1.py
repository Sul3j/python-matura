plik = open('napisy.txt', 'r')
wiersze = plik.readlines()

licznik_cyfry = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    for znak in wiersz:
        if znak.isdigit() == True:
            licznik_cyfry += 1

print('zadanie 4.1.')
print(licznik_cyfry)