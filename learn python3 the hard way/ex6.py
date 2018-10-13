# 这是运行的条件

# 这是一个变量
typws_of_people= 10
# 一个变量放到另一个字符串中
x = f"There are {types_of_people} types of people."

# 字符串变成变量
binary = "binary"
do_not = "don't"
# 变量放进字符串
y = f"Those who know {binary} and those who {do_not}."

# 这是运行的结果
print(x)
print(y)
# 再次格式化字符串
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
Joke_evaluation = "Isn't that joke so funny?! {}"

print(Joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
