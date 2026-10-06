#had to add the texts directly in here becaus filehandling is difrent between Windows and Unix and i dont have the time to work that out.

import tools

#define intro (pull text from a text file that explains the game and "story")
def intro():
    print("""200 years ago a temple filled
with treasure caved in...

Now it has been opened by thugs
to steal its treasure...

As the story told its filled
with door after door full of
old treasure and weapons.

But as it turns out its
also filled whit monsters who
now have goten out and started
terrorising the locals.

And if the whispers around town
are true, there is a HUGE gem
somewhere down there that
controls the monsters.

mayby if you find it we can
stop the monsters from hounting
the locals.

Good luck.""")
    tools.Continue()
    tools.ClearCLI()

#print logo
def logo():
    logo = """
            _______ _    _ ______    _____ _    _ ______  _____ _______                 
           |__   __| |  | |  ____|  / ____| |  | |  ____|/ ____|__   __|                
              | |  | |__| | |__    | |  __| |  | | |__  | (___    | |                   
              | |  |  __  |  __|   | | |_ | |  | |  __| \____ \   | |                   
              | |  | |  | | |____  | |__| | |__| | |____ ____) |  | |                   
              |_|  |_|  |_|______| \_____|\_____/|______|_____/   |_| 
  ______ ____  _____    _______ _____  ______     _     _____ _    _ _____  ______ 
 |  ____/ __ \|  __ \  |__   __|  __ \|  ____|   /\    / ____| |  | |  __ \|  ____|     
 | |__ | |  | | |__) |    | |  | |__) | |__     /  \  | (___ | |  | | |__) | |__        
 |  __|| |  | |  _  /     | |  |  _  /|  __|   / /\ \  \___ \| |  | |  _  /|  __|       
 | |   | |__| | | \ \     | |  | | \ \| |____ / ____ \ ____) | |__| | | \ \| |____      
 |_|    \____/|_|  \_\    |_|  |_|  \_\______/_/    \_\_____/ \____/|_|  \_\______|
 """
    print(logo)