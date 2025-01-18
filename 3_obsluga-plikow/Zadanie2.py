file = open("owoce.txt","r")

owoce = file.readline()

owoceLista = owoce.split(";")
owoceLista.pop()
print(owoceLista)

file.close()
