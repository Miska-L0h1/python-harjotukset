#kysyy leiviskät, naulat, luodit
num1 = float(input("Anna leiviskät. "))
num2 = float(input("Anna naulat. "))
num3 = float(input("Anna luodit. "))

num2 = num2 + num1*20
num3 = num3 + num2*32
gramma = num3*13.3

print("Massa nykymittojen mukaan:")
print(gramma/1000, "kilogrammaa ja", gramma, "gramma.")