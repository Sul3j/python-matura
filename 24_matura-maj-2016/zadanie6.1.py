plik = open('dane_6_1.txt', 'r')
wiersze = plik.readlines()

def szyfr_cezara(tekst, klucz):
    szyfr = ''
    for z in tekst:
        szyfr += chr(((ord(z) - 65 + klucz) % 26) + 65)
    return szyfr

zaszyfrowane = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    zaszyfrowane.append(szyfr_cezara(wiersz, 107))

plik.close()
plik = open("wynik_6_1.txt", "w")
for i in zaszyfrowane:
    plik.write(f"{i}\n")
plik.close()


