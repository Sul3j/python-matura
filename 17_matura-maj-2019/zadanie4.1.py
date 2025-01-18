plik = open("przyklad.txt", "r")
wiersze = plik.readlines()

ile = 0
tablica = []

def czyPotegaTrojki(liczba):
    potega = 0
    while liczba+1>(pow(3, potega)):
        if liczba==pow(3, potega):
            return True
        potega += 1
    return False

def czyPotegaTrojki2(liczba):
    tab = []
    potega = 0
    i = 0
    while True:
        if potega < 100000:
            potega = pow(3, i)
            tab.append(potega)
        else:
            break
        i += 1

    if liczba in tab:
        return True
    return False

for wiersz in wiersze:
    for i in wiersz.split():
        if i.isdigit():
            tablica.append(int(i))

for liczba in tablica:
    if czyPotegaTrojki(liczba):
        ile += 1

plik.close()
plik = open("wyniki4.txt", "w")
plik.write(f"4.1.\n{ile}")
plik.close()

