plik = open('dane_6_2.txt', 'r')
wiersze = plik.readlines()

wyniki = []

def szyfr_cezara(tekst, klucz):
    szyfr = ''
    for z in tekst:
        szyfr += chr(((ord(z) - 65 + klucz) % 26) + 65)
    return szyfr

for wiersz in wiersze:
    odszyfrowane = ''
    dane = wiersz.strip().split(' ')
    if len(dane) == 1:
        continue
    else:
        odszyfrowane = szyfr_cezara(dane[0], -int(dane[1]))

    wyniki.append(odszyfrowane)

plik.close()
plik = open("wynik_6_2.txt", "w")
for i in wyniki:
    plik.write(f"{i}\n")
plik.close()
