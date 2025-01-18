file = open("Plik2.txt","a")

i = 0
while i in range(10):
    a = input("Wprowadź cyfrę od 1 do 10 : ")
    file.write(a + "\n")
    i = i+1

file.close()