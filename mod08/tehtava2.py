#make set for names
names = set()
#while loop to add names till empty while checking if name is in the set already
name = input("Give name: ")
while name != "":
    if name in names:
        print("name already in the list")
    else:
        names.add(name)
        print("new name")
    name = input("Give name: ")
#print the names
print(names)