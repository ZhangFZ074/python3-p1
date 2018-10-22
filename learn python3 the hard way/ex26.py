print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv
script, filename = argv

txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
# 内置函数 input 录入用户输入的参数，> 为提示符，赋值给参数 file again
file_again = input("> ")
# 内置函数 open 打开参数 file again， 赋值给 txt again
txt_again = open(file_again)

print(txt_again.read())


print('Let\'s practice everything.')
print('You\'d need to know \'bout escapeswith \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 5
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars - 100
    return jelly_beans, jars, crates


start_point = 10000
# 定义函数 secret formula，参数 start_point，赋值给左边的参数
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# 函数 secret_formula的参数应该是有一定的调用或者赋值的
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")
# 需要注意的是最后一个if people=dogs要改成双等号(==)，来判断是否相等。如果还是单等号的话就是变量赋值，这样会报错的。
if people == dogs:
    print("People are dogs.")
