plik = open('identyfikator_przyklad.txt', 'r')
wiersze = plik.readlines()

palindromy = []

def czyPalindrom(text):
    if text == text[::-1]:
        return True
    else:
        return False

for wiersz in wiersze:
    wiersz = wiersz.strip()
    seria = wiersz[0:3]
    numer = wiersz[3:len(wiersz)]

    if czyPalindrom(seria) or czyPalindrom(numer):
        palindromy.append(wiersz)

plik.close()
plik = open('wyniki4.txt', 'a')
plik.write('\n\n4.2:\n')
for palindrom in palindromy:
    plik.write(f'{palindrom}\n')
plik.close()