# 导入 sys 模块
from sys import argv
# argv赋值给左边的变量，script是脚本名，filename是文件名
script, filename = argv
# open用于打开{filename}的txt文件
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = inpit(">")

txt_again = open(file_again)

print(txt_again.read())
