def znajdzLiczbyPierwsze(zakres):
    liczbyPierwsze = []
    for liczba in range(2, zakres):
        for liczbaPierwsza in liczbyPierwsze:
            if liczba % liczbaPierwsza == 0:
                break
        else:
            liczbyPierwsze.append(liczba)

    return liczbyPierwsze

liczbyPierwsze = znajdzLiczbyPierwsze(100)

def znajdzPare(liczba):
    for liczbaPierwsza in liczbyPierwsze:
        roznica = liczba - liczbaPierwsza
        if roznica in liczbyPierwsze:
            return (liczba, liczbaPierwsza, roznica)

plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()

odpowiedz = ""

for wiersz in wiersze:
    liczba = int(wiersz.split(" ")[0])
    wynik = znajdzPare(liczba)
    if liczba %  2 == 0:
        odpowiedz += f'''{wynik[0]} {wynik[1]} {wynik[2]} \n'''

plik.close()

plik = open("rozwiazania.txt", "w")

plik.write('4.1: \n\n')
plik.write(odpowiedz)

plik.close()

