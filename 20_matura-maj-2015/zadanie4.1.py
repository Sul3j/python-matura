plik = open("liczby.txt", "r")
wiersze = plik.readlines()

ilosc = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if wiersz.count('0') > wiersz.count('1'):
        ilosc += 1

plik.close()
plik = open("wyniki4.txt", "w")
plik.write(f"4.1: {ilosc}\n\n")
plik.close()
