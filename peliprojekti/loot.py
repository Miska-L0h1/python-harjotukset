import tools
import random

#define loot mechanic, bit long
def loot(player):
    print("""
    A chest? Open it
    
            🪎

    """)
    tools.Continue()
    tools.ClearCLI()
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
        tools.Continue()
        tools.ClearCLI()
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
        tools.Continue()
        tools.ClearCLI()
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
        tools.Continue()
        tools.ClearCLI()
    #empty
    elif chanse == 4:
        print("Its a empty :(")
        tools.Continue()
        tools.ClearCLI()
    return(player)

#define tresure, whit adaptivity as per gamemode
def tresure(player,mode,highscore):
    #infinite mode
    if mode == "yes":
        print("""
        ITS THE GEM!
                
            💎
            
        """)
        print("You found the gem!")
        player.score += 50
        print("+50 score")
        tools.Continue()
        tools.ClearCLI()
    #normal mode
    else:
        print("What is this?")
        print("\n")
        tools.Continue()
        print("oh!")
        print("\n")
        tools.Continue()
        print("""
            ITS THE GEM!
            
                💎
            
        """)
        player.score += 50
        print("You found the gem!")
        print("This is where the adventure ends.")
        tools.Continue()
        tools.ClearCLI()
        tools.end(player,highscore)

#define empty mechanic, nice and easy
def empty(player):
    print("The room is empty")
    #check that player doesnt get extra health
    if player.health + 1 <= player.maxhealth:
        player.health += 1
        print("+1 health")
    tools.Continue()
    tools.ClearCLI()
    return(player)