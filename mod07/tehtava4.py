#define list
nums = []
#define count to sum the numbers
def count(list):
    num = 0
    for i in list:
        num = num + i
    return(num)
#ask nums
num = input("Give a number: ")
#if num is empty stop
while num != "":
    nums.append(int(num))
    num = input("Give a number: ")
#print
print("")
print(count(nums))
