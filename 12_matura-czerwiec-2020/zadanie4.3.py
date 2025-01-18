def czyParaJestMniejsza(obecnaMinPara, sprawdzanaPara):
    liczbaObecnaMinPara = int(obecnaMinPara[0])
    slowoObecnaMinPara = obecnaMinPara[1].strip()
    liczbaSprawdzanaPara = int(sprawdzanaPara[0])
    slowoSprawdzanaPara = sprawdzanaPara[1].strip()

    if liczbaSprawdzanaPara != len(slowoSprawdzanaPara):
        return False
    if liczbaSprawdzanaPara < liczbaObecnaMinPara:
        return True
    if liczbaSprawdzanaPara == liczbaObecnaMinPara and slowoSprawdzanaPara < slowoObecnaMinPara:
        return True

    return False

plik = open("przyklad.txt", "r")
wiersze = plik.readlines()

minPara = wiersze[0].split(" ")
for wiersz in wiersze:
    paraDoSprawdzenia = wiersz.split(" ")
    if czyParaJestMniejsza(minPara, paraDoSprawdzenia):
        minPara= paraDoSprawdzenia

plik.close()

plik = open("rozwiazania.txt", "a")
plik.write('\n4.3:\n\n')
plik.write(f'''{minPara[0]} {minPara[1].strip()}''')

plik.close()