plik = open('identyfikator_przyklad.txt', 'r')
wiersze = plik.readlines()

maxSuma = 0
maxNumery = []

for wiersz in wiersze:
    sumaCyfr = 0
    wiersz = wiersz.strip()
    for i in range(3, len(wiersz)):
        sumaCyfr = sumaCyfr + int(wiersz[i])
    if sumaCyfr > maxSuma:
        maxSuma = sumaCyfr
        maxNumery.clear()
        maxNumery.append(wiersz)
    elif sumaCyfr == maxSuma:
        maxNumery.append(wiersz)


plik.close()
plik = open('wyniki4.txt', 'w')
plik.write('4.1:\n')
for numer in maxNumery:
    plik.write(f'{numer}\n')
plik.close()

