plik = open('punkty.txt', 'r')
wiersze = plik.readlines()

wynik = 0

def czy_cyfropodobne(punktX, punktY):
    punktyX = []
    punktyY = []

    for x in punktX:
        punktyX.append(x)

    for y in punktY:
        punktyY.append(y)

    if set(punktyX) == set(punktyY):
        return True
    return False


for wiersz in wiersze:
    wiersz = wiersz.strip().split(' ')
    if czy_cyfropodobne(wiersz[0], wiersz[1]):
        wynik += 1

plik.close()
plik = open('wyniki4.txt', 'a')
plik.write(f'\n\n4.2: {wynik}')
plik.close()
