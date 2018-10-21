print("let's pwactice everything.")
# 打印字符串，使用了转义字符单引号和反斜杠
print('You\'d need to know\'bout escapes with \\ that do:')
# 使用了转义字符换行符和水平制表符
print('\n newlines and \t tabs.')
# 使用了三个双引号，可以任意输入多行文本
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------")
print(poem)
print("----------")
# 将数学运算的结果赋值给变量 five
five = 10 - 2 + 3 - 6
print(f"This should be five {five}")
# 定义函数 sectet formula ，参数started
def secret_formula(started):
    # started 乘 500赋值给变量 jelly beans
    jelly_beans = started * 500
    # jelly beans 除 1000赋值给变量 jars
    jars = jelly_beans / 1000
    # jars 除 100赋值给变量crates
    crates = jars / 100
    # 返回函数的三个值
    return jelly_beans, jars, crates
# 将1000赋值给变量
start_point = 10000
# 函数secret formula，参数start point，赋值给三个变量
beans, jars, crates = secret_formula(start_point)

# 格式化用法，调用函数 format 将变量数值传入占位符 {} 中
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# It's just like with an f"" string
# 格式话用法，f 将占位符的参数打印为数值
print(f"We d have {beans} beans, {jars} jars, and {crates} crates.")
# 改变变量的值
start_point = start_point / 10

print("We can slso do that this way:")
# fomula = secret_formula(start_point)
# 函数 secret_formula， 参数 start_point，赋值给变量formula
formula = secret_formula(start_point)
# this is an easy way to apply a list to format string 
# 这是一种将列表应用于格式化字符串的简便方法
#print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
print("We'd have {} beans,{} jars,and {} crates.".format(*formula))
