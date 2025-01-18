owoce = open("owoce.txt", "a")
i = 0

while i in range(5):
    owoc = input("Podaj owoc : ")
    owoce.write(owoc + ";")
    i = i + 1

owoce.close()