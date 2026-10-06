#press to continue
def Continue():
    _ = input("<press enter to continue>")

#clear commandline
def ClearCLI() -> None:
    print("\033[H\033[J", end="")

#end screen
def end(player,highscore):
    print(f"""
__________________________
Game over:

your highscore: {highscore}

your score: {player.score}
__________________________
    """)
    exit()