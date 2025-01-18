plik = open("dane.txt", "r")
wiersze = plik.readlines()

odpowiedz = 0
obraz = []

for wiersz in wiersze:
    temp = wiersz.strip().split(" ")
    obraz.append([int(x) for x in temp])

for x in range(200):
    if obraz[x][::] != obraz[x][::-1]:
        odpowiedz += 1

plik.close()
plik = open("wyniki6.txt", "a")
plik.write(f"6.2: {odpowiedz}\n\n")
plik.close()