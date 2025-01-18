plik = open("sygnaly.txt", "r")
wiersze = plik.readlines()

odpowiedzSlowo = ""
odpowiedzMaks = 0

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if len(set(wiersz)) > odpowiedzMaks:
        odpowiedzSlowo = wiersz
        odpowiedzMaks = len(set(wiersz))

plik.close()
plik = open("wyniki4.txt", "a")
plik.write(f"\n\n4.2: {odpowiedzSlowo} {odpowiedzMaks}")
plik.close()
