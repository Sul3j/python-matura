plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

def binarne_na_dziesietne(liczba):
    x = 0
    pom = len(liczba)
    for i in range(len(liczba)):
        if liczba[i] == '1':
            x = x + 2 ** (pom - 1)
        pom -= 1
    return x

def cyfry(liczba):
    zbior = set()
    while liczba > 0:
        cyfra = liczba % 10
        zbior.add(cyfra)
        liczba //= 10
    return zbior

ilosc = 0
maxLiczba = 0
wyniki = 0
for wiersz in wiersze:
    wiersz = wiersz.strip()
    dziesietna = binarne_na_dziesietne(wiersz)
    rozne = cyfry(dziesietna)
    czy = 0 not in rozne
    if czy == 1:
        ilosc += 1
    if sum(rozne) > maxLiczba:
        maxLiczba = sum(rozne)
        wyniki = dziesietna

plik.close()

plik = open('wyniki3.txt', 'a')
plik.write('\n3.4:\n')
plik.write(f'{ilosc}\n')
plik.write(str(wyniki))
