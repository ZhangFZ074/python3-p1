i = 0
numbers = []
# 当变量 i 大于等于 6 时， while 将停止
while i < 6:
    # print("At the top i is %a" % i)
    print (f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now:", numbers)
    # print("At the bottom i is %a" % i)
    print(f"At the bottom i is {i}")

print("The numbers:")

for num in numbers:
    print(num)
