plik = open("przyklad.txt", "r")
wiersze = plik.readlines()

instrukcje = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    instrukcje.append(wiersz.split(" "))

instrukcje.sort()

ciag = 0
maxDlugosc = -1
maxLitera = ""

for x in range(0, len(instrukcje)-1, +1):
    if instrukcje[x][0] == "DOPISZ":
        ciag += 1
        if instrukcje[x][0] == instrukcje[x+1][0] and instrukcje[x][1] != instrukcje[x+1][1]:
            if ciag > maxDlugosc:
                maxDlugosc = ciag
                maxLitera = instrukcje[x][1]
            ciag = 0

plik.close()

plik = open("rozwiazanie.txt", "a")

plik.write("\n\n4.3: \n")
plik.write(maxLitera + " " + str(maxDlugosc))

plik.close()