def szyfr_cezara(wiadomosc, klucz):
    zaszyfrowana_wiadomosc = ''

    for x in wiadomosc:
        if x.isalpha():
            liczba = ord(x)
            liczba += klucz
            if x.isupper():
                if liczba > 90:
                    liczba -= 26
                elif liczba < 65:
                    liczba += 26
            else:
                if liczba > 122:
                    liczba -= 26
                elif liczba < 97:
                    liczba += 26
            zaszyfrowana_wiadomosc += chr(liczba)
        else:
            zaszyfrowana_wiadomosc += x

    return zaszyfrowana_wiadomosc


# 1 - zamieniamy literę na kod ascii
# 2 - zamieniamy ten kod asci na pozycję w alfabecie odejmując 65
# 3 - dodajemy klucz
# 4 - robimy operację reszty z dzielenia przez 26 aby liczba mieściła się w zakresie alfabetu
# 5 - zamieniamy pozycje w alfabecie na kod ascii dodając 65
# 6 - metodą chr zamieniamy liczbę z kodu ascii na literę

def szyfr_cezara_zawijanie(tekst, klucz):
    szyfr = ''
    for z in tekst:
        if z.isalpha():
            if z.isupper():
                szyfr += chr(((ord(z) - 65 + klucz) % 26) + 65)
            else:
                szyfr += chr(((ord(z) - 97 + klucz) % 26) + 97)
        else:
            szyfr += z
    return szyfr


print('Podaj swoja wiadomosc:')
wiadomosc = input()

print('Podaj swoj klucz:')
klucz = int(input())

print(szyfr_cezara_zawijanie(wiadomosc, klucz))
