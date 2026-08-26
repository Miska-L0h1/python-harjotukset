#Ask month
month = float(input("What month (number): "))

#do da season tubles
spring =(2, 3, 4)
summer = (5, 6, 7)
autumn = (8, 9, 10)
winter = (11, 12, 1)

#its a if and elif statement that does the month noticing you'll get it
if month in spring:
    print("its spring!")
elif month in summer:
    print("its summer!")
elif month in autumn:
    print("its autumn!")
elif month in winter:
    print("its winter!")
#just in case some degenerate answers "20" or sum
else:
    print("error")