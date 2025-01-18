plik1 = open('przyklad1.txt', 'r')
plik2 = open('przyklad2.txt', 'r')

wiersze1 = plik1.readlines()
wiersze2 = plik2.readlines()

posortowane = []

def sortowanie_przez_scalanie(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        R = tab[mid:]
        sortowanie_przez_scalanie(L)
        sortowanie_przez_scalanie(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k+=1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1

        return tab

for i in range(len(wiersze1)):
    dane = []
    for a in wiersze1[i].strip().split():
        dane.append(int(a))
    for b in wiersze2[i].strip().split():
        dane.append(int(b))

    posortowane.append(sortowanie_przez_scalanie(dane))

plik1.close()
plik2.close()

plik = open('wynik4_4.txt', 'w')
for i in posortowane:
    plik.write(f'{i} \n')
plik.close()