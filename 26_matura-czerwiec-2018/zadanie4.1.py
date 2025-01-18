plik1 = open('dane1.txt')
plik2 = open('dane2.txt')

wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()

wynik = 0

for i in range(len(wiersze1)):
    if wiersze1[i].strip().split()[9] == wiersze2[i].strip().split()[9]:
        wynik += 1

plik1.close()
plik2.close()

plik = open('wynik4_1.txt', 'w')
plik.write(f'{wynik}')
plik.close()