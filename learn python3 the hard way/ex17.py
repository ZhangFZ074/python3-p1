from sys import agrv           # 导入 sys 模块，argv（变量参数） 保存运行脚本时的参数
from os.path import exists     # 导入 os.path 模板

script, from_file, to_file = argv  # (解包)argv赋值给左边的三个变量

print(f"Copying from {from_file} to {to_file}")

in_file = opwn(from_file)      # open 函数打开变量 from file ，并赋值给变量 in file
indata = in_file.read()        # 变量 in file 调用 read 函数（读取文件内容）并把结果赋值给变量 indata

print(f"The inpue file is {len(indata)} bytes ling")   # len（）函数会以数值的形式返回的字符串长度

print(f"Does the output file exist? {exists(to_file)}")
print("Rwady, hit RETURN to continue, CTRL_C to abort.")
input()

out_file = open(to_file, 'w')  # 用 open 函数打开变量 to file，
out_file.write(indata)         # 在变量 out file 调用 write 函数，写入变量 indata 内容

print("Alright, all done.")

out_file.close()                # 调用 close  函数关闭文件
in_file.close()
