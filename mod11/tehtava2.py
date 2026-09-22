import random
#the race
class Race:
    def __init__(self, name):
            self.racename = name,
    
    def hourpass(self, cars):
        for car in cars:
            car.accele(random.randint(-10, 15))
            car.travel(1)
    def printstats(self, cars):
        for car in cars:
            print("-"*26)
            print("Car:", car.registration)
            print("Km driven: ",car.miles, "Km")
            print("Car's max speed: ", car.maxspeed, "Km/h")
        print("-"*26)

#define class auto
class Auto:
    #set values
    def __init__(self,regist,speed,maxx,miles):
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
class ElectricCar(Auto):
    def __init__(self, register, speed,maxspeed, battery):
        self.battery = battery,
        super().__init__(register,speed,maxspeed,0,)
class PetrolCar(Auto):
    def __init__(self, register, speed,maxspeed, fuel):
        self.fuel = fuel,
        super().__init__(register,speed,maxspeed,0,)

race = Race("Big car test")
#create cars
cars = []
cars.append(ElectricCar("ABC-15", 100 ,180, 52.5))
cars.append(PetrolCar("ACD-123", 100,  165, 32.3))

for i in range(3):
    race.hourpass(cars)
race.printstats(cars)