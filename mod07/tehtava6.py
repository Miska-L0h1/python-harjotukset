import math
#define function
def pizza(diameter,price):
    #define radius
    radius = diameter/2
    area = math.pi*radius**2
    #convert area into m from cm
    area = area/10000
    pm2=price/area
    return(pm2)
#ask the pizza info
pizza1size = float(input("What size is pizza num 1 (cm): "))
pizza1price = float(input("What price is pizza num 1 (€): "))
pizza2size = float(input("What size is pizza num 2 (cm): "))
pizza2price = float(input("What price is pizza num 2 (€): "))

pizza1 = pizza(pizza1size,pizza1price)
pizza2 = pizza(pizza2size,pizza2price)

if pizza1 < pizza2:
    print("pizza 1 is cheaper")
elif pizza1 > pizza2:
    print("pizza 2 is cheaper")
elif pizza1 == pizza2:
    print("both pizzas are the same price")
else:
    print("error")