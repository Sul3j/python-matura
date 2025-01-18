plik = open("pierwsze.txt", "r")
wiersze = plik.readlines()

daneTab = []

def waga(x):
    sum = 0
    sum_tmp = 0
    for i in str(x):
        sum += int(i)
    while sum >= 10:
        sum_tmp = sum
        sum = 0
        for i in str(sum_tmp):
            sum += int(i)
    return sum

for wiersz in wiersze:
    wiersz = wiersz.strip()
    daneTab.append(int(wiersz))

odpowiedz = 0

for i in daneTab:
    if waga(i) == 1:
        odpowiedz += 1

plik.close()

plik = open("wyniki4.txt", "a")

plik.write(f"\n\n4.3: {odpowiedz}")

plik.close()