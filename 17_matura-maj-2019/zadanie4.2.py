plik = open("przyklad.txt", "r")
wiersze = plik.readlines()

tablica = []
wyniki = []

def silnia(liczba):
    if liczba < 0:
        return None
    elif liczba == 0:
        return 1
    else:
        wynik = 1
        for i in range(1, liczba + 1):
            wynik *= i
        return wynik

def czySilnia(liczba):
    suma = 0
    while liczba != 0:
        suma += silnia(liczba % 10)
        liczba = liczba // 10
    return suma

for wiersz in wiersze:
    for i in wiersz.split():
        if i.isdigit():
            tablica.append(int(i))

for liczba in tablica:
    if czySilnia(liczba) == liczba:
        wyniki.append(liczba)

plik.close()
plik = open("wyniki4.txt", "a")
plik.write('\n\n4.2.\n')
for w in wyniki:
    plik.write(f"{w}\n")
plik.close()
