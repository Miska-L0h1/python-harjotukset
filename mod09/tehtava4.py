import random
#define class
class Auto:
    #set values
    def __init__(self, maxx, speed, regist, miles):
        self.registration = regist
        self.miles = miles
        self.maxspeed = maxx
        self.speednow = speed

    #kiihdytys = accelerating
    #define acceleration
    def accele(self, num):
        if self.speednow + num >= 0:
            if self.speednow + num <= self.maxspeed:
                self.speednow += num
            elif self.speednow + num == self.maxspeed:
                self.speednow += num
            else:
                self.speednow = self.maxspeed
        else:
            self.speednow = 0
    #kulje = travel
    #define travel
    def travel(self, num):
        self.miles += self.speednow * num

#create cars
cars = []
for i in (range(10)):
    register = "ABC-" + str(i+1)
    cars.append(Auto(random.randint(100,200), 60, register, 0))

finished = False

#the race loop
while finished == False:
    for car in cars:
        car.accele(random.randint(-10, 15))
        car.travel(1)
        if car.miles > 9999:
            finished = True

#print stats after finnish
for car in cars:
    print("-"*26)
    print("Car:", car.registration)
    print("Km driven: ",car.miles, "Km")
    print("Car's max speed: ", car.maxspeed, "Km/h")
print("-"*26)