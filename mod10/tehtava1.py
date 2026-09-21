class Elevator:
    def __init__(self, top, bottom):
        self.TopFloor = top
        self.BottomFloor = bottom
        self.CurrentFloor = bottom
    #define going floors, its quite elementary
    def GoToFloor(self, floor):
        if floor > self.CurrentFloor:
            for i in range(floor):
                self.FloorUp(1)
        elif floor < self.CurrentFloor:
            for i in range(self.CurrentFloor - floor):
                self.FloorDown(1)
        else:
            print("same floor")
        return
    #well, it defines Floorup and the one below defines floor down
    def FloorUp(self, num):
        if self.CurrentFloor + num <= self.TopFloor:
            self.CurrentFloor = self.CurrentFloor + num
            print(f"Current floor: {self.CurrentFloor}")
        return
    def FloorDown(self, num):
        if self.CurrentFloor - num >= self.BottomFloor:
            self.CurrentFloor = self.CurrentFloor - num
            print(f"Current floor: {self.CurrentFloor}")
        return


h = Elevator(10, 0)
h.GoToFloor(7)
h.GoToFloor(0)