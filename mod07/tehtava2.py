import random
#ask the sides
sides = int(input("how many sides on the dice? "))
#create dice throw function
def dice(side):
    throw = random.randint(1,side)
    return(throw)
#throw untill max side is hit while printting
throw = dice(sides)
while throw != sides:
    print(throw)
    throw = dice(sides)
print(throw)