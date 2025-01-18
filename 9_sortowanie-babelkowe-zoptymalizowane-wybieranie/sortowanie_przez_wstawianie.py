tab = [8, 2, 1, 9, 5]

i = 1

# iterujemy po wszystkich elementach tablicy
while i < len(tab):
    # do klucza przypisujemy element z którym będziemy porównywać
    key = tab[i]
    # do j przypisujęmy iterator o 1 mniejszy od iteratra liczby z którym porównujemy
    j = i-1
    # sprawdzamy czy 2 iterator jest większy lub równy 0 i klucz jest mniejszy od liczby porównywanej
    while j >= 0 and key < tab[j]:
        # jeśli tak to przesówamy liczbę o jedno miejsce
        tab[j+1] = tab[j]
        j -= 1
    # zmieniamy 1 liczbę z lewej na wartość klucza
    tab[j+1] = key
    i += 1
    # print(tab)
print(tab)
