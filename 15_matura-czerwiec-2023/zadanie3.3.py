plik = open('przyklad.txt', 'r')
wiersze = plik.readlines()


def binarne_na_dziesietne(liczba):
    x = 0
    pom = len(liczba)
    for i in range(len(liczba)):
        if liczba[i] == '1':
            x = x + 2 ** (pom - 1)
        pom -= 1
    return x


def dziesietne_na_binarne(liczba):
    s = ''
    while liczba > 0:
        if liczba % 2 == 1:
            s += '1'
        else:
            s += '0'
        liczba //= 2
    s = s[::-1]
    return s

roznica = 0
for i in range(len(wiersze)-1):
    w1 = wiersze[i].strip()
    w2 = wiersze[i+1].strip()
    x1 = binarne_na_dziesietne(w1)
    x2 = binarne_na_dziesietne(w2)
    if abs(x1-x2)>roznica:
        roznica = abs(x1-x2)

plik.close()

plik = open("wyniki3.txt", "a")
plik.write("\n3.3:\n")
plik.write(dziesietne_na_binarne(roznica))

plik.close()
