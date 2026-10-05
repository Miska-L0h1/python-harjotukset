import tools

#define intro (pull text from a text file that explains the game and "story")
def intro():
    with open("peliprojekti/texts/intro.txt") as file:
        txt = file.readlines()
        line_count = 0
    #print the text line by line 5 at a time
    for line in txt:
        #check if line is empty, so the text is easyer to read bit by bit
        if line != "\n":
            #the [0:-1 is so the lines print together]
            print(line[0:-1])
        else:
            tools.Continue()
            tools.ClearCLI()

#print logo
def logo():
    with open("peliprojekti/texts/logo.txt") as file:
        logo = file.read()
        print(logo)