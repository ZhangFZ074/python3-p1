# 这是一个格式化模板，搞不太清楚为什么要这样
formatter = "{} {} {} {}"

print(formatter.fomat(1, 2, 3, 4))
print(formatter.fomat("one", "two", "three", "four"))
print(formatter.fomat(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, fomatter))
print(formatter.format(
     "Try your",
     "Own text here",
     "Maybe a poem",
     "Or a song about fear"
))
