plik = open("przyklad.txt", "r")
wiersze = plik.readlines()

tablica = []
dlugoscCiagu = 0
poczatkowy = 0
nwdLiczb = 0

def nwd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a


for wiersz in wiersze:
    for i in wiersz.split():
        if i.isdigit():
            tablica.append(int(i))

for i in range(0, len(tablica)-1):
    dlugosc = 1
    poczatek = 0
    j = i
    nwdTmp = tablica[j]
    while nwd(nwdTmp, tablica[j+1]) != 1:
        dlugosc += 1
        nwdTmp = nwd(nwdTmp, tablica[j+1])
        if poczatek == 0:
            poczatek=tablica[j]
        j += 1
    if dlugosc > dlugoscCiagu:
        dlugoscCiagu = dlugosc
        nwdLiczb = nwdTmp
        poczatkowy = poczatek

plik.close()
plik = open("wyniki4.txt", "a")
plik.write("\n4.3.\n")
plik.write(f"dlugosc: {str(dlugoscCiagu)}\n")
plik.write(f"nwd: {str(nwdLiczb)}\n")
plik.write(f"pierwsza liczba ciagu: {str(poczatkowy)}\n")
plik.close()