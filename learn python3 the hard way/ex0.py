'''
python # 在powershell终端中运行python。
quit() # 键入quit(),退出python。
mkdir lpthw # 在powershell中创建一个目录。
cd lpthw # 在powershell中变到一个目录。
dir # 在powershell中列出目录。
'''
print("Hens", 25 + 30 / 6) # 数字不用加引号
print("Roosters", 100 - 25 * 3 % 4) # 逗号是分隔的作用。
print(3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6)
# 是真（真）还是假（ false）呢？
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7) # False
print("What is 3 + 2?", 3 + 2)
print("Is it greater?", 5 > -2)
print("Is it less or equal?", 5 <= -2)

########### 变量 ###############
cars = 100  # 变量
drivers = 50
print("There are", cars, "cars available.")
cars_not_driven = cars - drivers  # 变量也可以运算
print("There will be", cars_not_driven, "empty cars today.")