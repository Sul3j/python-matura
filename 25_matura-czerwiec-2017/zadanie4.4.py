plik = open('punkty.txt', 'r')
wiersze = plik.readlines()

wewnatrz = 0
zewnatrz = 0
brzegu = 0

def czy_wewnatrz(punkt):
    x = int(punkt[0])
    y = int(punkt[1])
    return (x > -5000 and x < 5000) and (y > -5000 and y < 5000)


def czy_na_brzegu(punkt):
    x = int(punkt[0])
    y = int(punkt[1])
    return (((x == -5000 or x == 5000) and (y >= -5000 and y <= 5000)) or ((y == -5000 or y == 5000) and (x >= -5000 and x <= 5000)))


for wiersz in wiersze:
    wiersz = wiersz.strip().split()

    if czy_wewnatrz(wiersz):
        wewnatrz += 1
    elif czy_na_brzegu(wiersz):
        brzegu += 1
    else:
        zewnatrz += 1

plik.close()
plik = open('wyniki4.txt', 'a')
plik.write('\n\n4.4:\n')
plik.write(f'wewnatrz: {wewnatrz}\n')
plik.write(f'z brzegu: {brzegu}\n')
plik.write(f'na zewnatrz: {zewnatrz}')
plik.close()