#This one is like your script with argv
# 这个就像你的argv脚本，argv是就像是线性链接，args是串行链接
def print_two(*args):
    arg1,arg2=args
    print(f"arg1:{arg1},arg2:{arg2}")

#Ok,that *argv is actually pointless,we can just do this
#ok，* args实际上毫无意义，我们可以做到这一点
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

#This just takes one argument
#这只需要一个参数
def print_one(arg1):
    print(f"arg1:{arg1}")

#This one takes no arguments
#这个没有参数
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
