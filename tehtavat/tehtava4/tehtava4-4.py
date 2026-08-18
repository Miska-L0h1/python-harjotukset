#kysyy vuoden
vuosi = int(input("Anna vuosi. "))

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("vuosi",vuosi,"on karkausvuosi")
        else:
            print("vuosi",vuosi,"ei ole karkausvuosi")
    else:
        print("vuosi",vuosi,"on karkausvuosi")
else:
    print("vuosi",vuosi,"ei ole karkausvuosi")