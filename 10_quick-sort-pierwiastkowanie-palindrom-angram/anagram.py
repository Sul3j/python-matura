def czy_anagramy(a, b):
    return "tak" if sorted(a) == sorted(b) else "nie"

# głowna część programu
a = input()
b = input()
print(czy_anagramy(a, b))