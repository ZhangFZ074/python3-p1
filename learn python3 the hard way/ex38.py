ten_things = "Apples Oranges Crows Telephone Light Sugar"
# 说明
print("Wait there are not 10 things in that list.Lrt's fix that.")
# 切割
stuff = ten_things.split(' ')  # 在括号里面的字符串删除
# 列表
more_stuff = ["Day", "Night" "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
# 
while len(stuff) != 10:
    # pop 移除列表中的一个数字，默认最后一位
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    # append 在列表后面追加元素
    stuff.append(next_one)
    print(f"There are {len(stuff)} item now.")

print("There wo go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print('#'.join(stuff[3:5]))
