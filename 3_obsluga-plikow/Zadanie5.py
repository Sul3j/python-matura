file = open("Plik2.txt","r")

list = []

for i in range(10):
    list.append(int(file.readline()))

print(list)

# nie wiem co dalej