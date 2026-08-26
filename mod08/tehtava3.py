#make dictionary of airports
airports = {}
#ask what to do
answer = input("add (airport), search (airport) or quit? ")
while answer != "quit":
    #ask the airport ICAO code and name
    if answer == "add":
        airport = input("give name for an airport: ")
        code = input("give ICAO code for an airport: ")
        airports[code] = airport
    #search dictionary for airports
    elif answer == "search":
        airport = input("what ICAO-code is the airport? ")
        if airport in airports:
            print(f"{airport} is: {airports[airport]}")
    #ask what to do
    answer = input("add (airport), search (airport) or quit? ")