#while looppi joka kysyy tuumia ja kääntää ne senteiksi kunnes tuuma on negatiivinen
tuuma = float(input("Anna tuuma. "))
while tuuma > 0:
    print(tuuma, "tuuma on", tuuma * 2.54, "cm")
    tuuma = float(input("Anna uusi tuuma. "))