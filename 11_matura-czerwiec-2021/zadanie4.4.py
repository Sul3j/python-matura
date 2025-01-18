plik = open('napisy.txt', 'r')
wiersze = plik.readlines()

haslo = ''

for wiersz in wiersze:
    wiersz = wiersz.strip()
    liczba1 = -1
    liczba2 = -1

    for znak in wiersz:
        if znak.isdigit() and liczba1 == -1:
            liczba1 = znak
        elif znak.isdigit():
            liczba2 = znak
            ascii = liczba1 + liczba2

            if int(ascii) >= 65 and int(ascii) <= 90:
                litera = chr(int(ascii))
                haslo += litera
            liczba1 = -1
            liczba2 = -1

    if haslo.endswith('XXX'):
        break

print('zadanie 4.4.')
print(haslo)