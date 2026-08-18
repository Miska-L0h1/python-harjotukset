#kysy sukupuoli
sex = input("mikä on biologinen sukupuolesi? ")
hemogl = int(input("mikä on biologinen sukupuolesi? "))

#laskee ne
if sex == "Mies":
    if hemogl < 134:
        print("sulla on alhainen hemoglobiiniarvo")
    elif hemogl > 195:
        print("sulla on korkea hemoglobiiniarvo")
    else:
        print("sulla on normaali hemoglobiiniarvo")
elif sex == "Nainen":
    if hemogl < 117:
        print("sulla on alhainen hemoglobiiniarvo")
    elif hemogl > 175:
        print("sulla on korkea hemoglobiiniarvo")
    else:
        print("sulla on normaali hemoglobiiniarvo")
else:
    "jokin meni pieleen :()"