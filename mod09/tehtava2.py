#define class
class Auto:
    #set values
    def __init__(self, maxx, speed, miles, regist):
        auto.registration = regist
        auto.miles = miles
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

#set values
auto = Auto(142, 0, "ABC-123", 0)

#do the acceleration
auto.accele(30)
auto.accele(70)
auto.accele(50)
auto.accele(-200)