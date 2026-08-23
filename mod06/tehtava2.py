nums = []
num = input("Give a number: ")
while num != "":
    nums.append(num)
    num = input("Give a number: ")
nums.sort(reverse=True)
times = 0
for numero in nums:
    if times != 5:
        print(numero)
        times = times + 1