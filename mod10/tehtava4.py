import random
#define class race
class Race:
    def __init__(self, name, length, many):
        self.racename = name,
        self.racelength = length
        self.manycars = many

    def hourpass(self, cars):
        finished = False
        while finished == False:
            for car in cars:
                car.accele(random.randint(-10, 15))
                car.travel(1)
                if car.miles > self.racelength:
                    finished = True
    def printstats(self, cars):
        for car in cars:
            print("-"*26)
            print("Car:", car.registration)
            print("Km driven: ",car.miles, "Km")
            print("Car's max speed: ", car.maxspeed, "Km/h")
        print("-"*26)
    def raceover():
        pass
#define class auto
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


race = Race("Suuri romuralli",8000,10)
#create cars
cars = []
for i in (range(race.manycars)):
    register = "ABC-" + str(i+1)
    cars.append(Auto(random.randint(100,200), 60, register, 0))

race.hourpass(cars)
race.printstats(cars)