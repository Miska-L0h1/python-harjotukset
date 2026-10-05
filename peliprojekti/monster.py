
import tools
import random

#define monser
class Monster():
    def __init__(self,icon, hp, damage, armor):
        self.icon = icon
        self.hp = hp
        self.maxhp = hp
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

#define monster, long and complicated
def monster(player,highscore):
    #get random monster skin
    monster_skins = ["🧌","🧟","👹","👾","🐉","🕷️"]
    #create monster
    monster = Monster(monster_skins[random.randint(1,6)-1],random.randint(1,4),(player.shield - random.randint(1,2)),(player.sword - random.randint(1,2)))
    print("Its a Monster!")
    #monster loop
    while True:
        print(f"""
        {"♥" * monster.hp}{"♡" * (monster.maxhp - monster.hp)}
        {monster.icon}
        {player.stats()}
        """)
        print("attack or block")
        choice = input("")
        #choice tree for attack/block
        if choice == "attack":
            monster.hp -= player.sword - monster.armor
            #just in case the monster fully blocks the hit, so it doenst acsidentaly give extra hp to it
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            print(f"{player.sword - monster.armor} damage to the monster!")
            if monster.hp > 0:
                monster_damage = monster.monster_damage()
                player.health -= monster_damage
                print(f"You took {monster_damage} damage from the monster!")
            tools.Continue()
            tools.ClearCLI()
        elif choice == "block":
            monster_damage = monster.monster_damage()
            player.health -= monster_damage - player.shield
            #just in case the shield full block the hit, so it doenst acsidentaly give extra hp
            if player.health > player.maxhealth:
                player.health = player.maxhealth
            if monster_damage - player.shield >= 0:
                print(f"You took {monster_damage - player.shield} damage from the monster!")
            else:
                print(f"you blocked the monsters hit!")
                if random.randint(1,4) == 4:
                    if player.health + 2 <= player.maxhealth:
                        player.health += 2
                        print("you healed 2 health")
                    elif player.health + 1 <= player.maxhealth:
                        player.health += 1
                        print("you healed 1 health")
            hitback = monster_damage - monster.armor
            if hitback > 0:
                monster.hp -= hitback
                print(f"{hitback} damage bounced back to the monster!")
            tools.Continue()
            tools.ClearCLI()
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
            tools.Continue()
            break
        #check if player dead
        if player.health <= 0:
            print("You died.")
            tools.Continue()
            tools.end(player,highscore)
            exit()