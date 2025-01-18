tab = [7, 3, 2, 8, 6]

i = 0
swap = True


# jeśli dochodzi do jakichkowiek zamian to jest ta pętla kontynuowana
while i < len(tab) - 1 and swap:
    j = 0
    swap = False
    # odejmujemy i aby nie sprawdzać liczb które są na końcu i są już pewne
    while j < len(tab) - 1 - i:
        if tab[j] > tab[j+1]:
            tmp = tab[j]
            tab[j] = tab[j+1]
            tab[j+1] = tmp
            swap = True
        j+=1
    i+=1
    #print(tab)

print(tab)