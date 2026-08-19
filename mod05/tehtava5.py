#define user and password
user = "python"
passwrd = "rules"
wrong_pass = 0

#ask pass and user
user_inpt = input("username: ")
passwrd_inpt = input("password: ")
#print empty row for cleaner output
print("")

#loop to check if user and pass are correct
while user_inpt != user or passwrd_inpt != passwrd:
    if wrong_pass == 5:
        print("Pääsy evätty")
        break
    user_inpt = input("username: ")
    passwrd_inpt = input("password: ")
    #print empty row for cleaner output
    print("")
    wrong_pass = wrong_pass + 1

#check if the pass and user is right
if user_inpt == user or passwrd_inpt == passwrd:
    print("Tervetuloa")