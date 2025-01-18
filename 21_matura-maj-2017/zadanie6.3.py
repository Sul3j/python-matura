plik = open("dane.txt", "r")
wiersze = plik.readlines()

obraz = []

odpowiedz = 0

# sąsiedzi prawy/lewy/dolny/górny
koordynaty = ((1,0), (-1,0), (0,1), (0,-1))

for wiersz in wiersze:
    temp = wiersz.strip().split(" ")
    obraz.append([int(x) for x in temp])

for x in range(0, 320):
    for y in range(0, 200):
        licznik = 0
        for k in koordynaty:
            if x + k[0] > 319 or x + k[0] < 0 or y + k[1] > 199 or y + k[1] < 0:
                continue
            else:
                if abs(obraz[y][x] - obraz[y + k[1]][x + k[0]]) > 128:
                    licznik += 1
        if licznik != 0:
            odpowiedz += 1

plik.close()
plik = open("wyniki6.txt", "a")
plik.write(f"6.3: {odpowiedz}\n\n")
plik.close()