class House:
    def __init__(self, top, bottom):
        self.TopFloor = top
        self.BottomFloor = bottom
        self.Elevators = []
    

class Elevator:
    def __init__(self, House):
        self.CurrentFloor = House.bottom
    def GoToFloor(self, floor):
        if floor > self.CurrentFloor:
            for i in range(floor):
                self.FloorUp(1)
        elif floor < self.CurrentFloor:
            for i in range(self.CurrentFloor - floor):
                self.FloorDown(1)
        else:
            print("MY BROTHER IN CHRIST ITS THE SAME FLOOR")
        return
    def FloorUp(self, House, num):
        if self.CurrentFloor + num <= House.TopFloor:
            self.CurrentFloor = self.CurrentFloor + num
            print(f"Current floor: {self.CurrentFloor}")
        return
    def FloorDown(self, num):
        if self.CurrentFloor - num >= House.BottomFloor:
            self.CurrentFloor = self.CurrentFloor - num
            print(f"Current floor: {self.CurrentFloor}")
        return

house = House(10, 0)
h = Elevator()
h.GoToFloor(7)
h.GoToFloor(0)