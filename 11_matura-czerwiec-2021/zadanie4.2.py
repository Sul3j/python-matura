plik = open('napisy.txt', 'r')
wiersze = plik.readlines()

haslo = ''
index = 0

for i in range(19, len(wiersze), 20):
    haslo += wiersze[i][index]
    index += 1

print('zadanie 4.2.')
print(haslo)