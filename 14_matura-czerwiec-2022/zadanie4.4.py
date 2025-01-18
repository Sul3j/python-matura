plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

liczby = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    liczby.append(wiersz)

bezPowtorzen = []
licznikWystapien = []

for i in range(len(liczby)):
    if liczby[i] not in bezPowtorzen:
        licznikWystapien.append([liczby[i], liczby.count(liczby[i])])
        bezPowtorzen.append(liczby[i])

rozne = len(licznikWystapien)
dwaRazy = 0
trzyRazy = 0

for i in licznikWystapien:
    if i[1] == 2:
        dwaRazy+=1
    if i[1] == 3:
        trzyRazy+=1

plik.close()

plik = open('wyniki4.txt', 'a')

plik.write(f'\n4.4:\n\n{str(rozne)} {str(dwaRazy)} {str(trzyRazy)}')

plik.close()