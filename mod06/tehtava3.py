#ask the number, create range number and create list
number = int(input("Give a number: "))
rangernum = number + 1
deviders = []
checker = ""
#go through all the numbers until the given numeber and add them into a list
for i in range(1,rangernum):
    if number % i == 0:
        deviders.append(int(i))
#go through the list
for i in deviders:
    if i == 1 or i == number:
        checker = checker
    else:
        checker = "no"
if checker == "no":
    print("not a prime number")
else:
    print("prime number")