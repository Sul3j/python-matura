import math

plik = open('punkty.txt', 'r')
wiersze = plik.readlines()

max = 0
punkty = []

def odleglosc_miedzy_punktami(a, b):
    return abs(math.sqrt((int(b[0]) - int(a[0])) ** 2 + (int(b[1]) - int(a[1])) ** 2))

for i in range(0, len(wiersze)):
    for j in range(0, len(wiersze)):
        a = wiersze[i].strip().split()
        b = wiersze[j].strip().split()
        if odleglosc_miedzy_punktami(a, b) > max:
            max = odleglosc_miedzy_punktami(a, b)
            punkty = [a, b]

plik.close()
plik = open('wyniki4.txt', 'a')
plik.write('\n\n4.3:')
plik.write(f'\nmax odleglosc: {round(max)}')
plik.write(f'\npunkty: {punkty[0]}, {punkty[1]}')
plik.close()

