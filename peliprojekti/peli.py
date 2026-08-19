# ask name
name = input("Hei! Mikä on nimesi? ")
age = int(input("Kuinka vanha olet? "))
# kick under 12 year old off
if age > 12:
    exit
print("hi", name)

#ask for command
print("komennot:    odota      syö     nuku     lopeta")
command = input("anna komento: ")
while command != "lopeta":
    if command == "odota":
        print("odotetaan")
    elif command == "syö":
        print("nam nam nam")
    elif command == "odota":
        print("Zzzzz")
    print("komennot:    odota      syö     nuku     lopeta")
    command = input("anna komento: ")