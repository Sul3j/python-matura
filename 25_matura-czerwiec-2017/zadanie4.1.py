plik = open('punkty.txt', 'r')
wiersze = plik.readlines()

wynik = 0

def czyPierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    if czyPierwsza(int(wiersz[0])) and czyPierwsza(int(wiersz[1])):
        wynik += 1

plik.close()
plik = open('wyniki4.txt', 'w')
plik.write(f'4.1: {wynik}')
plik.close()