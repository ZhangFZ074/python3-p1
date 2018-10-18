from sys import argv            # 导入 sys 模块
script, input_file = argv       # 解包赋值

def print_all(f):               # 自定义函数 print all
    print(f.read())             # 让 f 调用 read 函数

def rewind(f):                  # 自定义函数 rewind
    f.seek(0)                   # 让 f 调用 seek 函数

def print_a_line(line_count,f):     # 自定义函数 print a line
    print(line_count,f.readline())  # 让 f 调用 readline 函数

current_file = open(input_file)     # 函数 open 打开变量input file 赋值给current file

print("First let's peint the whole dile:\n")    # 打印全部字符串并换行
print_all(current_file)                         # 自定义函数（参数）

print("Now let's rewind, kind of like a tape.")
rewind(current_file)                            # 自定义函数（参数）

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line=current_line+1 
print_a_line(current_line,current_file)

current_line=current_line+1 
print_a_line(current_line,current_file) 
