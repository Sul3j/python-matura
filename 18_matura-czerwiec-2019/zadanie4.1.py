plik = open("liczby_przyklad.txt", "r")
wiersze = plik.readlines()

daneTab = []

def czyPierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


for wiersz in wiersze:
    wiersz = wiersz.strip()
    daneTab.append(int(wiersz))

odpowiedzi = []

for i in daneTab:
    if i>=100 and i<=5000 and czyPierwsza(i):
        odpowiedzi.append(i)

plik.close()

plik = open("wyniki4.txt", "w")

plik.write("4.1:\n\n")

for i in odpowiedzi:
    plik.write(f"{i}\n")

plik.close()