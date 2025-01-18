plik = open('liczby.txt', 'r')
wiersze = plik.readlines()

odbicia = []
podzielne17 = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    odbicia.append(int(wiersz[::-1]))

for odbicie in odbicia:
    if odbicie % 17 == 0:
        podzielne17.append(str(odbicie))

plik.close()

plik = open('wyniki4.txt', 'w')

plik.write(f'4.1:\n\n')

for i in podzielne17:
    plik.write(f'{i} ')

plik.close()
