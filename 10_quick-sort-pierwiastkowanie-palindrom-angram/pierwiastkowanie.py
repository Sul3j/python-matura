def pierwiastkowanie(n):
    a = 1
    b = n
    eps = .000001  # liczba miejsc po przecinku
    while abs(a - b) >= eps:  # sprawdzamy, czy osiągnięto oczekiwaną precyzję
        a = (a + b) / 2  # długość boku "a" wyznaczamy ze średniej arytmetycznej liczb a i b
        b = n / a  # długość boku "b" wyznaczamy ze wzoru na pole

    return (a + b) / 2

print(f'{pierwiastkowanie(int(input())):.6f}')