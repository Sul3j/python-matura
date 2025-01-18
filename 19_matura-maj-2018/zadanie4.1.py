plik = open("sygnaly.txt", "r")
wiersze = plik.readlines()

odpowiedz = ""
licznik = 1

for wiersz in wiersze:
    wiersz = wiersz.strip()
    if licznik % 40 == 0:
        odpowiedz += wiersz[9]
    licznik += 1

plik.close()
plik = open("wyniki4.txt", "w")
plik.write(f"4.1: {odpowiedz}")
plik.close()

