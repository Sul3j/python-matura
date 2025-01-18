plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

def czyPierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

liczby = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    liczby.append(wiersz)

liczbyPierwsze = []

for liczba in liczby:
    if czyPierwsza(int(liczba)) and czyPierwsza(int(liczba[::-1])):
        liczbyPierwsze.append(liczba)

plik.close()

plik = open('wyniki4.txt', 'a')

plik.write('\n\n4.3:\n\n')

for liczbaPierwsza in liczbyPierwsze:
    plik.write(f'{liczbaPierwsza} ')

plik.close()