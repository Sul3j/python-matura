plik = open("pierwsze.txt", "r")
wiersze = plik.readlines()

daneTab = []

def czyPierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


for wiersz in wiersze:
    wiersz = wiersz.strip()
    daneTab.append(int(wiersz[::-1]))

odpowiedzi = []

for i in daneTab:
    if czyPierwsza(i):
        odpowiedzi.append(str(i)[::-1])

plik.close()

plik = open("wyniki4.txt", "a")

plik.write("\n\n4.2:\n\n")

for i in odpowiedzi:
    plik.write(f"{i}\n")

plik.close()