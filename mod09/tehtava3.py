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
        print(f"speed now is: {self.speednow} km/h")
    #kulje = travel
    #define travel
    def travel(self, num):
        self.miles += self.speednow * num
        print(self.miles)


#set values
auto = Auto(142, 60, "ABC-123", 0)

#do the acceleration
auto.travel(1.5)