plik = open("sygnaly.txt", "r")
wiersze = plik.readlines()

odpowiedz = list()

for wiersz in wiersze:
    wiersz = wiersz.strip()
    string = "".join(sorted(wiersz))
    if ord(string[len(string)-1])-ord(string[0])<=10:
        odpowiedz.append(wiersz)

plik.close()
plik = open("wyniki4.txt", "a")
plik.write(f"\n\n4.3:\n\n")
for odp in odpowiedz:
    plik.write(f"{odp}\n")
plik.close()