import random
#Ask number of points
points = int(input("How many points? "))
#create variables for counters
cycles = 0
inside = 0
#while loop until x amount of cycles are compleet
while cycles <= points:
#generate random cordinates and then check them
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    if x**2+y**2<1:
        inside = inside + 1
    cycles = cycles + 1
#print approximation of pi
print(4*inside/points)