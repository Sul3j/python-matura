ciag = "AlaMakotaAKotMaAle"

duze = ciag.upper()

duzeLitery = []

dlugosc = len(ciag)

i = 0

while i < dlugosc :
    if ciag[i] == duze[i] :
        duzeLitery.append(duze[i])
    i = i + 1
duzeLitery.sort()

print(duzeLitery)