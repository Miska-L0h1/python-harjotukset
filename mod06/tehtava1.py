#import random for the dice
import random

num = int(input("How many dice? "))
dice = 0

#throw the dice
for x in range(num):
    dice = dice + random.randint(1,6)

#print the sum
print(dice)