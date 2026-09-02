#define class
class Auto:
    pass
#set values
auto = Auto()
auto.registration = "ABC-123"
auto.maxspeed = "142 km/h"
auto.miles = "0 km"
auto.speednow = "0 km/h"
#print (propably could have been 4 difrent print commands but im stubborn)
print(f"car's register number is: {auto.registration} \ncar's max speed is: {auto.maxspeed} \ncar's driven distance is: {auto.miles} \ncar's current speed is: {auto.maxspeed} \n")