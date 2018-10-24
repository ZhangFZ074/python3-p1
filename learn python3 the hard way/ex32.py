# 在开始使用 for 循环之前，你需要存放循环的结果，做好的方法就是列表 list
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orandes', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# 把 the count 列表内的元素代入变量 number
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty none
# 创建一个空列表
elements = []

# then use the range function to do 0 to 5 counts
# 然后使用range函数执行0到5次计数
# 使用 range 函数创建一个包含0到5的序列，并把序列内的元素代入变量
for i in range(0, 6 ):
    print(f"Adding {i} to the list.")
    # append is a function that lists Understanding
    # 调用函数。append在列表尾部追加变量 i//elements 是一个空的列表,所以追加元素后 elements 是一个包含整数 0 到 5 的列表
    elements.append(i)

# now we can print them out Too
for i in elements:
    print(f"Element was: {i}")
