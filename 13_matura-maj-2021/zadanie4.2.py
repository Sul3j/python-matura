plik = open("przyklad.txt", "r")
wiersze = plik.readlines()

instrukcje = []

for wiersz in wiersze:
    wiersz = wiersz.strip()
    instrukcje.append(wiersz.split(" ")[0])

ciag = 0
maxInstrukcja = ""
maxDlugosc = -1

for i in range(0, len(instrukcje)-1, +1):
    ciag += 1
    if instrukcje[i+1] != instrukcje[i]:
        if ciag > maxDlugosc:
            maxDlugosc = ciag
            maxInstrukcja = instrukcje[i]
        ciag = 0

plik.close()

plik = open("rozwiazanie.txt", "a")
plik.write("\n\n4.2: \n")
plik.write(maxInstrukcja + " " + str(maxDlugosc))
plik.close()