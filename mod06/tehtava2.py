#make list and ask first num
nums = []
num = input("Give a number: ")
#if num is empty stop
while num != "":
    nums.append(int(num))
    num = input("Give a number: ")
#sort the list
nums.sort(reverse=True)
#set up counter to 5
times = 0
for numero in nums:
    if times != 5:
#print 5 times
        print(numero)
        times = times + 1