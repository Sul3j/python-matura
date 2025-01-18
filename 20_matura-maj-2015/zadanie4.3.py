plik = open("liczby.txt", "r")
wiersze = plik.readlines()

nrWiersza = 0
minStr = str()
maxStr = str()
minLinia = 0
maxLinia = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    nrWiersza += 1
    if len(minStr) == 0:
       maxStr = wiersz
       minStr = wiersz
       maxLinia = nrWiersza
       minLinia = nrWiersza
    if wiersz > maxStr and len(wiersz) >= len(maxStr):
        maxStr = wiersz
        maxLinia = nrWiersza
    if wiersz < minStr and len(wiersz) <= len(minStr):
        minStr = wiersz
        minLinia = nrWiersza

plik.close()
plik = open("wyniki4.txt", "a")
plik.write(f"4.3: min: {minLinia} max: {maxLinia}\n\n")
plik.close()


