#define list
nums = []
#define count to filter the numbers
def count(list):
    nums = []
    for i in list:
        if i % 2 == 0:
            nums.append(i)
    return(nums)

num = input("Give a number: ")
#if num is empty stop
while num != "":
    nums.append(int(num))
    num = input("Give a number: ")
#print
print("")
print(nums)
print(count(nums))