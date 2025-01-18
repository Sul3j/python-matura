def czy_palindrom(n):
    i = 0; j = len(n) - 1 # ustawiam na pierwszą i ostatnią literę
    while i < j:
       if n[i] != n[j]:  # jeśli mamy niezgodność liter
           return "nie"
       i += 1
       j -= 1
    return "tak" # jeśli wszystkie litery stoją na odpowiednich pozycjach

# głowna część programu
print(czy_palindrom(input()))

def czy_palindrom2(n):
   return "tak" if n == n[::-1] else "nie"

# głowna część programu
print(czy_palindrom(input()))