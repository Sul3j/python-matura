plik = open("dane.txt", "r")
wiersze = plik.readlines()

pikselMin = -1
pikselMax = -1

obraz = []

for wiersz in wiersze:
    temp = wiersz.strip().split(" ")
    obraz.append([int(x) for x in temp])

for x in range(200):
    for y in range(320):
        if obraz[x][y] > pikselMax or pikselMax == -1:
            pikselMax = obraz[x][y]
        if obraz[x][y] < pikselMin or pikselMin == -1:
            pikselMin = obraz[x][y]

plik.close()
plik = open("wyniki6.txt", "w")
plik.write(f"6.1: min: {pikselMin} max: {pikselMax}\n\n")
plik.close()


