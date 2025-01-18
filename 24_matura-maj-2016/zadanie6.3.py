plik = open('dane_6_3.txt', 'r')
wiersze = plik.readlines()

wyniki = []

def szyfr_cezara(tekst, klucz):
    szyfr = ''
    for z in tekst:
        szyfr += chr(((ord(z) - 65 + klucz) % 26) + 65)
    return szyfr

for wiersz in wiersze:
    dane = wiersz.strip().split(' ')
    prawidlowy = False
    if len(dane) == 1:
        continue
    for k in range(0, 26):
        szyfr = szyfr_cezara(dane[0], k)
        if szyfr == dane[1]:
            prawidlowy = True
    if prawidlowy == False:
        wyniki.append(dane[0])

plik.close()
plik = open("wynik_6_3.txt", "w")
for i in wyniki:
    plik.write(f"{i}\n")
plik.close()