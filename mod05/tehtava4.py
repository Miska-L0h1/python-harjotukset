import random

#generoi luku
luku = random.randint(1,10)
#kysyy lukua
arvaus = int(input("Arvaa luku 1-10 välillä "))
#kun arvattu luku ei ole THE luku looppaa
while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    arvaus = int(input("Arvaa luku 1-10 välillä "))
print("Oikein")