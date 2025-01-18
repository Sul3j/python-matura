def znajdzNajdluzszyCiagZnakow(slowo):
    obecnaLitera = slowo[0]
    maksymalnaDlugoscLancucha = 1
    licznikWystapien = 1
    wynik = (obecnaLitera * maksymalnaDlugoscLancucha, maksymalnaDlugoscLancucha)

    for i in range(1, len(slowo)):
        if obecnaLitera == slowo[i]:
            licznikWystapien += 1
        else:
            licznikWystapien = 1
            obecnaLitera = slowo[i]

        if licznikWystapien > maksymalnaDlugoscLancucha:
            maksymalnaDlugoscLancucha = licznikWystapien
            wynik = (obecnaLitera * maksymalnaDlugoscLancucha, maksymalnaDlugoscLancucha)

    return wynik

plik = open("przyklad.txt", "r")
wiersze = plik.readlines()
odpowiedz = ""

for wiersz in wiersze:
    slowo = wiersz.split(" ")[1]
    wynikFunkcji = znajdzNajdluzszyCiagZnakow(slowo)
    odpowiedz += f'''{wynikFunkcji[0]} {wynikFunkcji[1]} \n'''

plik.close()

plik = open("rozwiazania.txt", "a")
plik.write('\n4.2:\n\n')
plik.write(odpowiedz)
plik.close()