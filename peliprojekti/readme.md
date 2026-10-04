## The quest for treasure

Miska Lohikoski

## The idea
The idea is to find the lost gem from a caved in temple now opened.
By finding the lost gem the player can stop the monsters attacking local villagers.

## (the non infinite mode) The goal:
the goal is to find a mystical gem 💎 (before that you need 50 score)

## How to play:

at start of the game you are asked few things:

your age:
if under 12 you will be kicked off the game, dont lie.
your name.
and if you want to play infinite mode?
infinite mode is basicly the same game ast the normal but after finding the game continues.
if your goal is to reach highest score posible to impress ALL of your friends then inifinte mode allows you to max out that highscore.
by default the game will use the normal mode, where the game ends when you find the gem.

The game is quite simple to play and will tell the player what to do whit instuctions like:
"<press enter to continue>" and "pick another door" and "attack or block"
As seen in the last example the game might ask player to input an answer, in that case its always told what the expected input is, either attack or block in the examples case.

another example:
What door will you chose?
 ___    ___    ___  
| 1 |  | 2 |  | 3 |
|  *|  |  *|  |  *| 
|___|  |___|  |___|

the expected input is 1, 2 or 3. if the answer is not one of those you will be asked again.

# Monster battle

Battleing monsters is the most complicated mechanic in the game.
the fight will look like this:

            ♥♥♥♡
             👹

Player | score: 15 | highscore: 100
♥♥♥♥♥♡♡ | 🗡  6 dmg  | 🛡  5 armor

the most important thing you need to know is to keep eye on is your health displayed under your name
second most important is the monsters health.

based on these two things and also the damage of your sword and your shields armor
you should chose either **attack** the monster in wich case the monster will take damage and so will you.
or **block** the monsters attack, if the monsters damage is more powerfull than the monster armor the rest of it after the armor will be bounced back at the monster.
if you fully block the hit you will heal up to 2 health if needed.

## Sustainable development
Sustainable development goals the game is linked to is 16 Peace, Justice and Strong Institutions.

By finding the gem and stoping the hords of monsters from terrorising the locals you are bringing peace to the village.
"People everywhere should live free from fear and all forms of violence,
feeling safe as they go about their lives—regardless
of their ethnicity, faith, or sexual orientation."

How can the locals live free from fear and violence if there are monsters around?
thats right, they cant.

## File structure
the game is stored in the peli.py file.
sntro.txt holds as it name says the intro
save.txt holds the current highscore, it will regenerate if deleted but the progress will be lost.