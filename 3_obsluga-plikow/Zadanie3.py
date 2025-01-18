import os

if os.path.exists("Plik1.txt"):
    os.remove("Plik1.txt")
else:
    print("Dany plik nie istnieje")