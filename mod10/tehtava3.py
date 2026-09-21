 #Define all the Elevators
class Elevator:
    def __init__(self,  bottom):
        self.CurrentFloor = bottom
    def GoToFloor(self, House, floor):
        if floor > self.CurrentFloor:
            for i in range(floor):
                self.FloorUp(House, 1)
        elif floor < self.CurrentFloor:
            for i in range(self.CurrentFloor - floor):
                self.FloorDown(House, 1)
        else:
            print("Its the same floor.")
        return
    def FloorUp(self, House, num):
        if self.CurrentFloor + num <= House.TopFloor:
            self.CurrentFloor = self.CurrentFloor + num
            print(f"Current floor: {self.CurrentFloor}")
        return
    def FloorDown(self, House, num):
        if self.CurrentFloor - num >= House.BottomFloor:
            self.CurrentFloor = self.CurrentFloor - num
            print(f"Current floor: {self.CurrentFloor}")
        return

#define the house
class House:
    def __init__(self, top, bottom, num):
        self.TopFloor = top
        self.BottomFloor = bottom
        self.Elevators = [Elevator(bottom) for i in range(num)]

    def DriveElevator(self, drivele):
        print(f"Useing elevator {drivele}")
        floor = int(input("What floor are we going? "))
        self.Elevators[drivele].GoToFloor(self, floor)

    #da fire alarm
    def Firealarm(self):
        print("FIREALARM!!!")
        for i in len(self.Elevators):
            self.Elevators[i].GoToFloor(self, self.BottomFloor)
            print(f"elevator {i} is back on bottom floor")
        
        

Top = int(input("Top floor? "))
Bottom = int(input("Bottom floor? "))
Elevators = int(input("How many Elevators? "))

house = House(Top, Bottom, Elevators)

#print basic thinggy
print("")
print("Elevators:")
for i in range(Elevators):
    print(f"elevator {(i + 1)}")
drivele = int(input("Which elevator do you want to use? (number only) "))

#while loop for the elevator
while True:
    if drivele == "":
        house.Firealarm
    else:
        house.DriveElevator(drivele)

        print("")
        print("Elevators:")
        for i in range(Elevators):
            print(f"elevator {(i + 1)}")
        drivele = input("Which elevator do you want to use? (number only) " )