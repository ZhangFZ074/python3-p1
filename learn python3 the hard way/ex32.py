# 定义列表
# 列表可以放入数字和字符串
the_count = [1, 2, 3, 4, 5]
gruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 'dimes', 3, 'quarters']

# 把 the_count 列表内的元素代入 number，打印字符串
for number in the_count:
    print(f"This is count {number}")

for fruit in gruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

# 创建一个空列表
elements = []

# range() 函数可创建一个整数列表，一般用在 for 循环中。
# 把列表内的元素代入 i
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # 函数append在列表elements后面追加参数 i
    elements.append(i)

# 把 列表 elements 中的元素打印出来
for i in elements:
    print(f"Flements was: {i}")
