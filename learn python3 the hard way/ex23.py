# 导入 sys 模块
import sys
# sys 模块获取 argv 参数变量
script, encoding, error = sys.argv

# def 定义函数 main ，参数为 languafe file，encoding， errors。
def main(language_file, encoding, errors):
    # 调用函数 readline 读取文本文件中的一行 赋值给line
    line = language_file.readline()
    # 判断语句 line ，检测一个变量的值来决定一段代码的运行
    if line:
        # 调用了另一个函数来实际打印这一行
        print_line(line, encoding, errors)
        # 在 main 里面调用了一次 main ， 技术上讲不管函数在哪里，我们都能调用
        return main(language_file, encoding, errors)

# def 定义函数 print line ， 参数为 ling， encoing， errors
# 事实上他是对 languages.txt 中每一行进行编码
def print_line(line, encoding, errors):
    # 调用 strip 移除 line 字符串首位的字符（这里移除换行符）
    next_lang = line.strip()
    # 调用 encode 把 raw bytes 编码成字节串
    raw_bytes = next_lang.encode(encoding, errors = errors)
    # 调用 decode 把 raw bytes 编码成字符串
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    # 把 两个变量打印出来，看是什么样的
    print(raw_bytes, "<===>", cooked_string)
    # 打开 languagws.txt 文件
languages = open("languages.txt", encoding = "utf- 8")
# 执行 main 函数
main(languages, encoding, error)
