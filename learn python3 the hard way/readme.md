## 笨办法学 python3

> 学习的秘诀就是连续不断的重复

### 第一个程序
~~~
~~~
### 数字变量和注释
~~~
~~~
### 作出决定
> 嵌套式 if 语句，根据玩家 input 的内容，来 print 的内容。

- print
- variable 变量
- input
- if elif else

~~~
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the besr.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, dong {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothspins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool pf muck.")
        print("Good job!")

else:
    print("You stumble around and fall no a knife and die. Good job!")        
~~~
### 列表
- f-string # f"some stuff here {avariable}"
- range()  # 范围
- append() # 添加
- remove() # 删除指定值
- pop()    # 删除列表值
~~~
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
~~~
