#define converter
def converter(gal):
    l = gal*3.785
    return(l)
#ask gallons
gallon = float(input("How many gallons: "))
#convert until negative
while gallon > 0:
    liter = converter(gallon)
    print(liter)
    gallon = float(input("How many gallons: "))