plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

def silnia(liczba):
    x = 1
    for i in range(1, liczba+1):
        x = x * i
    return x

def kombinacje(k,n):
    x = silnia(n) / (silnia(k) * silnia(n-k))
    return x

def liczba_zer(liczba):
    ilosc = 0
    for i in range(len(liczba)):
        if liczba[i] == '0':
            ilosc += 1
    return ilosc

def max_anagram(ilosc):
    max = 0
    if ilosc > max:
        max = ilosc
    return max

z = 0
tab = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if len(wiersz) == 8:
        a = liczba_zer(wiersz)
        b = kombinacje(a, 7)
        c = max_anagram(b)
        if c == z:
            tab.append(wiersz)
        if c > z:
            z = c
            tab.clear()
            tab.append(wiersz)
            
plik.close()
plik = open('wyniki3.txt', 'a')
plik.write('\n\n3.2:\n')

for i in range(len(tab)):
    plik.write(f'{tab[i]}\n')
