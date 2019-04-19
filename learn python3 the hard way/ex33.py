# 将 0 赋值给变量 i
i = 0
# 创建一个空列表 numbers
numbers = []

# 判断布尔值表达式 i < 6 的真假，若为 True 则 whihe循环就会一直不停的执行它下面的代码块
while i < 6:
    # 打印下面带字符串
    print(f"At the top i is {i}")
    # 使用 append() 函数在 numbers 列表的尾部追加参数 i
    numbers.append(i)
    # 将 i + 1赋值给 i ,变量可以重复赋值
    i = i + 1
    # 打印字符串和列表
    print("Numbers now:",numbers)
    print(f"At the bottom i is {i}")

# 打印字符创
print("The numbers:")

# 把 numbers 列表中的元素代入 num ，然后打印、
# 这时候 列表里面有 6个数值，循环一次打印一个
for num in numbers:
    print(num)
