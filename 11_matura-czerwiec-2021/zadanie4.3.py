plik = open('napisy.txt', 'r')
wiersze = plik.readlines()

haslo = ''
for wiersz in wiersze:
    wiersz = wiersz.strip()
    opcja1 = wiersz + wiersz[0]
    opcja2 = wiersz[len(wiersz)-1] + wiersz

    if opcja1 == opcja1[::-1]:
        haslo += opcja1[(len(opcja1) - 1) // 2]

    elif opcja2 == opcja2[::-1]:
        haslo += opcja2[(len(opcja2) - 1) // 2]

print('zadanie 4.3.')
print(haslo)