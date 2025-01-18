tab = [8, 2, 1, 9, 5]

i = 0

# pętla iterująca po wszystkich elementach poza ostatnim
while i < len(tab) - 1:
    # tworzymy zmienną przechowującą index najmniejzej wartości w tablicy
    minIndex = i
    # ustawiamy iterator pętli wewnętrznej na element następny
    j = i + 1
    # iterujemy dopuki index elementu następnego jest mniejszy od długości tablicy
    while j < len(tab):
        # sprawdzanymy czy liczba najmniejsza jest jest większa od następnej
        if tab[minIndex] > tab[j]:
            # jeśli wrunek jest spełniony zamieniamy index najmniejszej liczby na index liczby następnej
            minIndex = j
        j += 1

    # zamieniamy pierwszą wybraną liczbę na liczbę najmniejszą
    tmp = tab[i]
    tab[i] = tab[minIndex]
    tab[minIndex] = tmp
    i+=1
    # print(tab)
print(tab)