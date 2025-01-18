plik1 = open('dane1.txt')
plik2 = open('dane2.txt')

wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()

wynik = 0

def proporcja(wiersz):
    parzyste = 0
    nieparzyste = 0
    for i in wiersz:
        if int(i) % 2:
            parzyste += 1
        else:
            nieparzyste += 1
    if parzyste == nieparzyste:
        return True
    return False

for i in range(len(wiersze1)):
    if proporcja(wiersze1[i].strip().split()) and proporcja(wiersze2[i].strip().split()):
        wynik += 1

plik1.close()
plik2.close()

plik = open('wynik4_2.txt', 'w')
plik.write(f'{wynik}')
plik.close()