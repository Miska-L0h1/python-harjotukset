import random
import tools
import texts
import monster
import loot

#get highscore from save file
try:
    with open("peliprojekti/save.txt") as file:
        highscore = int(file.read())
except:
    highscore = 0

#define player
class Player(): 
    def __init__(self,name):
        self.name = name
        self.health = 5
        self.maxhealth = 5
        self.sword = 3
        self.shield = 3
        self.score = 0
    def stats(self):
        return(f"""
{self.name} | score: {self.score} | highscore: {highscore}
{"♥" * self.health}{"♡" * (self.maxhealth - self.health)} | 🗡  {self.sword} dmg  | 🛡  {self.shield} armor""")

#define door mechanic, includes all the door related mechanics (adding this to its own file would be too complicated becaus it is essentially the mainloop of the gameplay as it calls all the other methods)
def doors(player):
    #print the door icons
    print(f"""
What door will you chose?
 ___    ___    ___  
| 1 |  | 2 |  | 3 |
|  *|  |  *|  |  *| 
|___|  |___|  |___|
{player.stats()}
    """)
    #to counter error of not inputing int
    while True:
        try:
            picked_door = int(input(""))
            if 0 < picked_door < 4:
                break
            else:
                print("pick 1, 2 or 3")
        except ValueError:
            print("enter the door number, just the number.")
    tools.ClearCLI()
    #set up the door mechanic variables
    doors_lock = [0, 0, 0]
    chanse = random.randint(1,100)
    #the door loop
    while True:
        #tresure mechanic (under 50 score directed to loot)
        if chanse < 11:
            if player.score >= 50:
                loot.tresure(player,infinite_mode,highscore)
            else:
                loot.loot(player)
            break
        #Lock mechanic
        elif 10 < chanse and chanse < 26:
            print("The door is locked")
            print("pick another door")
            doors_lock[picked_door-1] = 1 
            #to counter error of not inputing int
            while True:
                try:
                    picked_door = int(input(""))
                    break
                except ValueError:
                    print("enter the door number, just the number.")
            #check if 2/3 doors are locked
            lock_count = 0
            for i in doors_lock:
                if i == 1:
                    lock_count += 1
            #if 2 doors are locked, go to empty for new doors.
            if lock_count == 2:
                loot.empty(player)
            else:
                #check if the door has been asinged locked
                if doors_lock[picked_door-1] == 0:
                    chanse = random.randint(1,100)
                else:
                    print("Its still locked...")
                lock_count = 0
        #call empty
        elif 25 < chanse < 56:
            loot.empty(player)
            break
        #call monster
        elif 55 < chanse < 81:
            monster.monster(player,highscore)
            break
        #call loot
        else:
            loot.loot(player)
            break

#menu
texts.logo()

age = int(input("How old are you? "))
# kick under 12 year old off
if age < 12:
    print("the game is K12")
    print("the game will close itself now.")
    exit()

name = input("What is your name? ")

player = Player(name)

#infinite mode switch for an alternative game play
print("Do you want to play the infinite-mode?")
print("yes or no (default)")
infinite_mode = input("")
tools.ClearCLI()

#play the intro
texts.intro()

#The while loop
while True:
    doors(player)
    tools.ClearCLI()
    #make sure health doesnt surpass maxhealth stats
    if player.health > player.maxhealth:
        player.maxhealth = player.maxhealth
    #set score as highscore if its bigger than highscore
    if player.score > highscore:
        highscore = player.score
        with open("peliprojekti/save.txt", "w") as file:
            file.write(str(highscore))
    if player.health <= 0:
        tools.end(player,highscore)
        break