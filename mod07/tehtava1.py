import random
# define function to throw dice
def dice():
    throw = random.randint(1,6)
    return(throw)
# throw the dice
throw = dice()
# print until 6
while throw != 6:
    print(throw)
    throw = dice()
print(throw)