plik = open('identyfikator_przyklad.txt', 'r')
wiersze = plik.readlines()

niepoprawne = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    znak0 = (ord(wiersz[0])-55) * 7
    znak1 = (ord(wiersz[1])-55) * 3
    znak2 = (ord(wiersz[2])-55) * 1
    znak4 = int(wiersz[4]) * 7
    znak5 = int(wiersz[5]) * 3
    znak6 = int(wiersz[6]) * 1
    znak7 = int(wiersz[7]) * 7
    znak8 = int(wiersz[8]) * 3
    suma = znak0 + znak1 + znak2 + znak4 + znak5 + znak6 + znak7 + znak8
    suma = suma % 10

    if suma != int(wiersz[3]):
        niepoprawne.append(wiersz)

plik.close()
plik = open('wyniki4.txt', 'a')
plik.write('\n\n4.3:\n')
for ni in niepoprawne:
    plik.write(f'{ni}\n')
plik.close()
