tab = [8, 2, 1, 9, 5]

i = 0


while i < len(tab) - 1: # pętla iterująca po wszystkich elementach poza ostatnim
    j = 0
    while j < len(tab) - 1: # petla wykonująca ciąg porównań elemntu z elementem następnym
        # sprawdzamy czy następny element jest większy od poprzedniego
        if tab[j] > tab[j+1]:
            #gdy warunek jest spełniony zamieniamy je kolejnością
            tmp = tab[j]
            tab[j] = tab[j+1]
            tab[j+1] = tmp
        j+=1
    i+=1
    # print(tab)

print(tab)