plik1 = open('dane1.txt', 'r')
plik2 = open('dane2.txt', 'r')

wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()

ilosc = 0
wiersze = []

def czy_te_same_cyfry(wiersz1, wiersz2):
    takie_same = True
    dane1 = []
    dane2 = []
    for i in range(10):
        for a in wiersz1[i]:
            dane1.append(a)
        for b in wiersz2[i]:
            dane2.append(b)

    if set(dane1) != set(dane2):
        takie_same = False

    return takie_same

for i in range(len(wiersze1)):
    if czy_te_same_cyfry(wiersze1[i].strip().split(), wiersze2[i].strip().split()):
        wiersze.append(i + 1)
        ilosc += 1

plik1.close()
plik2.close()

plik = open('wynik4_3.txt', 'w')
plik.write(f'ilosc: {ilosc} / wiersze: {wiersze}')
plik.close()