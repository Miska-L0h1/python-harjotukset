import random
#define game over for the main while loop
over = 0
#get highscore from save file
try:
    with open("save.txt", "w") as file:
        og_score = int(file.read())
except:
    og_score = None
#make highscore 
if og_score != None:
    highscore = og_score
else:
    highscore = 0

class Player(): 
    def __init__(self,name):
        self.name = name
        self.health = 3
        self.maxhealth = 5
        self.sword = 10
        self.shield = 5
        self.score = 0


# define funcitons (prorject 3)
def doors(player):
    print("""
    What door will you chose?
     ___    ___    ___  
    | 1 |  | 2 |  | 3 |
    |  *|  |  *|  |  *| 
    |___|  |___|  |___|

    print(f"{player.name} | score:{player.score} | {"♥ " * player.health} | 🗡  {player.sword} dmg  | 🛡  {player.shield} armor")
    """)
    _ = int(input(""))
    chanse = random.randint(1,100)
    lock_count = 0
    while lock_count != 3:
        if chanse > 10:
            if player.score > 100:
                tresure(player)
            else:
                loot(player)
        elif 10 < chanse > 25:
            print("The door is locked")
            print("pick another door")
            _ = int(input(""))
            chanse = random.randint(1,100)
            lock_count =+ 1
        elif 25 > chanse > 55:
            empty()
            break
        elif 55 > chanse > 80:
            monster()
            break
        else:
            loot()
            break
    if lock_count = 3:
        print("all doors are locked.")
        print("This is where the adventure ends.")
        over = 1

def empty(player):
    print("The room is empty")
    if player.health < player.maxhealth  + 1:
        player.health = player.health + 1
        print("+1 health")
    return(player)

def loot(player):
    print("""
    A chest? Open it
    
            🪎

    """)
    _ = input("")
    chanse = random.randint(1,5)
    if chanse == 1:
        print("""
        Its a potion!
        
               𖠞
        
        """)
        if health < maxhealth  + 2:
                health = health + 2
                print("+2 health")
        else:
            maxhealth =+ 1
            health =+ 1
            print("+1 max health")
    elif chanse == 2:
        print("""
        Its a sword!
        
               🗡
        
        """)
        sword =+ 1
        print("+1 damage to the sword")
    elif chanse == 3:
        print("""
        Its a shield!
        
               🛡
        
        """)
        shield =+ 1
        print("+1 armor to the shield")
    elif chanse == 4:
        print("Its a empty :(")
    return(sword,shield,maxhealth)
def tresure():
    print("What is this?")
    print("oh!")
    print("""
        ITS THE GEM!
        
               💎
        
        """)
    print("You found the gem")
    print("This is where the adventure ends.")
    over = 1
def monster():
    pass
def over():
    print(f"""
    Game over:

    your highscore: {highscore}

    your score: {player.score}
    """)

age = int(input("How old are you? "))
# kick under 12 year old off
if age > 12:
    exit

name = input("Hi! what is your name? ")
print("hi", name)
print("hi", name)
name
#ask for
player = Player(name)

#ask for command (project 2)
command = input("give command: ")
while command != "quit":
    if command == "wait":
        health = wait(health,maxhealth)
    elif command == "eat":
        health = eat(health,maxhealth)
    elif command == "sleep":
        health = sleep(health,maxhealth)
    print(f"{name} | score:{score} | {"♥ " * health} | 🗡  {sword} dmg  | 🛡  {shield} armor")
    print("commands:    wait      eat     sleep     quit")
    command = input("give command: ")