plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

def zrownowazona(liczba):
    jedynki = 0
    zera = 0
    for i in range(len(liczba)):
        if liczba[i] == '1':
            jedynki += 1
        else:
            zera += 1

    if jedynki == zera:
        return 'tak'
    elif abs(jedynki - zera) == 1:
        return 'nie'

rownowaga = 0
prawie = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if zrownowazona(wiersz) == 'tak':
        rownowaga += 1
    elif zrownowazona(wiersz) == 'nie':
        prawie += 1

plik.close()

plik = open('wyniki3.txt', 'w')

plik.write('3.1:\n')
plik.write(f'{rownowaga}\n{prawie}')