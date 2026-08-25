import time
# define funcitons (prorject 3)
def wait(health,maxhealth):
    print("waiting")
    time.sleep(5)
    if health < maxhealth  + 1:
        health = health + 1
    return(health)
def eat(health,maxhealth):
    print("eating")
    time.sleep(2)
    if health < maxhealth + 1:
        health = health + 1
    return(health)
def sleep(health,maxhealth):
    print("sleeping")
    time.sleep(10)
    if health < maxhealth + 2:
        health = health + 2
    if health < maxhealth + 1:
        health = health + 1
    return(health)
# ask name (prorject 1)
name = input("Hei! Mikä on nimesi? ")
# ask age (prorject 2)
age = int(input("Kuinka vanha olet? "))
# kick under 12 year old off
if age > 12:
    exit
print("hi", name)

health = 3
maxhealth = 5
sword = 10
shield = 5
score = 0

#ask for command (project 2)
print(f"{name} | score:{score} | {"♥ " * health} | 🗡  {sword} dmg  | 🛡  {shield} armor")
print("commands:    wait      eat     sleep     quit")
command = input("give command: ")
while command != "quit":
    if command == "wait":
        health = wait(health,maxhealth)
    elif command == "eat":
        health = eat(health,maxhealth)
    elif command == "sleep":
        health = sleep(health,maxhealth)
    print(f"{name} | score:{score} | {"♥ " * health} | 🗡  {sword} dmg  | 🛡  {shield} armor")
    print("commands:    wait      eat     sleep     quit")
    command = input("give command: ")