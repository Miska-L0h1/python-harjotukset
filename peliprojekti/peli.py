#write the intro text and update the readme

import random

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

#define monser
class Monster():
    def __init__(self,icon, hp, damage, armor):
        self.icon = icon
        self.hp = hp
        self.dmg = damage
        self.armor = armor
    def monster_damage(self):
        chance = random.randint(1,3)
        if chance == 1:
            damage = self.dmg - 1
        elif chance == 2:
            damage = self.dmg
        elif chance == 3:
            damage = self.dmg + 1
        return(damage)

#define funcitons

#define intro (pull text from a text file that explains the game and "story")
def intro():
    with open("peliprojekti/intro.txt") as file:
        txt = file.readlines()
        line_count = 0
    #print the text line by line 5 at a time
    for line in txt:
        line_count += 1
        if line_count != 6:
            #the [0:-1 is so the lines print together]
            print(line[0:-1])
        else:
            skip()
            line_count = 0
            print("")
            print(line[0:-1])

#define skip (make player enter a input (enter) to proggress for clearer gameplay)
def skip():
    _ = input("<press enter to continue>")

#define door mechanic, includes all the door related mechanics
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
            break
        except ValueError:
            print("enter the door number, just the number.")
    #set up the door mechanic variables
    doors_lock = [0, 0, 0]
    chanse = random.randint(1,100)
    #the door loop
    while True:
        #tresure mechanic (under 50 score directed to loot)
        if chanse < 11:
            if player.score >= 50:
                tresure(player)
            else:
                loot(player)
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
                empty(player)
            else:
                #check if the door has been asinged locked
                if doors_lock[picked_door-1] == 0:
                    chanse = random.randint(1,100)
                else:
                    print("Its still locked...")
                lock_count = 0
        #call empty
        elif 25 < chanse < 56:
            empty(player)
            break
        #call monster
        elif 55 < chanse < 81:
            monster(player)
            break
        #call loot
        else:
            loot(player)
            break

#define empty mechanic, nice and easy
def empty(player):
    print("The room is empty")
    #check that player doesnt get extra health
    if player.health + 1 <= player.maxhealth:
        player.health += 1
        print("+1 health")
    skip()
    return(player)

#define loot mechanic, bit long
def loot(player):
    print("""
    A chest? Open it
    
            🪎

    """)
    skip()
    chanse = random.randint(1,4)
    #potion
    if chanse == 1:
        print("""
        Its a potion!
        
               𖠞
        
        """)
        #check that player doesnt get extra health while checking if player is less than max health
        if player.health + 2 <= player.maxhealth:
                player.health += 2
                print("+2 health")
        #add 1 to max and norm health
        else:
            player.maxhealth += 1
            player.health += 1
            print("+1 max health")
        #add to score
        player.score += 5
        print("+5 score")
        skip()
    #sword
    elif chanse == 2:
        print("""
        Its a sword!
        
               🗡
        
        """)
        #add damage to sword and add scored
        player.sword += 1
        player.score += 5
        print("+5 score")
        print("+1 damage to the sword")
        skip()
    #shield
    elif chanse == 3:
        print("""
        Its a shield!
        
               🛡
        
        """)
        #add 1 to shield and 5 to score
        player.shield += 1
        print("+1 armor to the shield")
        player.score += 5
        print("+5 score")
        skip()
    #empty
    elif chanse == 4:
        print("Its a empty :(")
        skip()
    return(player)

#define tresure, whit adaptivity as per gamemode
def tresure():
    #infinite mode
    if infinite_mode == "yes":
        print("""
        ITS THE GEM!
                
            💎
            
        """)
        print("You found the gem!")
        player.score += 50
        print("+50 score")
        skip()
    #normal mode
    else:
        print("What is this?")
        print("\n")
        skip()
        print("oh!")
        print("\n")
        skip()
        print("""
            ITS THE GEM!
            
                💎
            
        """)
        print("You found the gem!")
        print("This is where the adventure ends.")
        skip()
        end()

#define monster, long and complicated
def monster(player):
    #get random monster skin
    monster_skins = ["🧌","🧟","👹","👾","🐉","🕷️"]
    #create monster
    monster = Monster(monster_skins[random.randint(1,6)-1],random.randint(1,4),random.randint(1,2),random.randint(1,3))
    print("Its a Monster!")
    #monster loop
    while True:
        print(f"""
        {"♥ " * monster.hp}
        {monster.icon}
        {player.stats()}
        """)
        print("attack or block")
        choice = input("")
        #choice tree for attack/block
        if choice == "attack":
            monster.hp -= player.sword - monster.armor
            print(f"{player.sword - monster.armor} damage to the monster!")
            if monster.hp > 0:
                monster_damage = monster.monster_damage()
                player.health -= monster_damage
                print(f"You took {monster_damage} damage from the monster!")
            skip()
        elif choice == "block":
            monster_damage = monster.monster_damage()
            player.health -= monster_damage - player.shield
            #just in case the shield full block the hit, so it doenst acsidentalygive extra hp
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            print(f"You took {monster_damage - player.shield} damage from the monster!")
            hitback = round(monster_damage * 0.25) - monster.armor
            if hitback > 0:
                monster.hp -= hitback
                print(f"{hitback} damage bounced back to the monster!")
            skip()
        else:
            continue
        print("\n")
        #check if monster is dead
        if monster.hp <= 0:
            print("You killed the monster")
            player.health += 2
            print("+2 health")
            player.score += 20
            print("+20 score")
            skip()
            break
        #check if player dead
        if player.health <= 0:
            print("You died.")
            skip()
            end()
#end screen
def end():
    print(f"""
    Game over:

    your highscore: {highscore}

    your score: {player.score}
    """)

#print game name:
print("""
    _______ _    _ ______    _____ _    _ ______  _____ _______           
   |__   __| |  | |  ____|  / ____| |  | |  ____|/ ____|__   __|          
      | |  | |__| | |__    | |  __| |  | | |__  | (___    | |             
      | |  |  __  |  __|   | | |_ | |  | |  __|  \___ \   | |             
      | |  | |  | | |____  | |__| | |__| | |____ ____) |  | |             
  ____|_|__|_| _|_|______|__\_____|\____/|______|_____/   |_|____  ______ 
 |  ____/ __ \|  __ \  |__   __|  __ \|  ____|/ ____| |  | |  __ \|  ____|
 | |__ | |  | | |__) |    | |  | |__) | |__  | (___ | |  | | |__) | |__   
 |  __|| |  | |  _  /     | |  |  _  /|  __|  \___ \| |  | |  _  /|  __|  
 | |   | |__| | | \ \     | |  | | \ \| |____ ____) | |__| | | \ \| |____ 
 |_|    \____/|_|  \_\    |_|  |_|  \_\______|_____/ \____/|_|  \_\______|
                                                                          
""")

#menu
age = int(input("How old are you? "))
# kick under 12 year old off
if age > 12:
    exit

name = input("What is your name? ")

player = Player(name)

#infinite mode switch for an alternative game play
print("Do you want to play the infinite-mode?")
print("yes/no")
infinite_mode = input("")

#play the intro
intro()

#The while loop
while True:
    doors(player)
    #make sure health doesnt surpass maxhealth stats
    if player.health > player.maxhealth:
        player.maxhealth = player.maxhealth
    #set score as highscore if its bigger than highscore
    if player.score > highscore:
        highscore = player.score
        with open("peliprojekti/save.txt", "w") as file:
            file.write(str(highscore))
    if player.health <= 0:
        end()
        break