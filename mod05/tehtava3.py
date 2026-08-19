#tehään muutujat
luku = (input("Anna luku. "))
isoin = luku
pienin = luku
#loop kunne luku on tyhjä
while luku != "":
    if luku > isoin:
        isoin = luku
    elif luku < pienin:
        pienin = luku
    luku = (input("Anna uusi luku. "))
#printataan suurin ja pienin
print("pienin luku oli:", pienin, "suurin luku oli:", isoin)