plik = open("dane.txt", "r")
wiersze = plik.readlines()

obraz = []

maxCiag = 0

for wiersz in wiersze:
    temp = wiersz.strip().split(" ")
    obraz.append([int(x) for x in temp])

for y in range(0, 320):
    z = 1
    for x in range(1, 200):
        if obraz[x-1][y] == obraz[x][y]:
            z += 1
        else:
            if z > maxCiag:
                maxCiag = z
            z = 1

plik.close()
plik = open("wyniki6.txt", "a")
plik.write(f"6.4: {maxCiag}\n\n")
plik.close()