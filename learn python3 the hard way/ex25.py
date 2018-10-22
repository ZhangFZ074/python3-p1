# 定义函数 break words，参数stuff
def break_words(stuff):
    # 文档注释，（这个函数会为我们分解单词）
    """This function will bresk up words for us."""
    # 参数 stuff 调用函数 split 分解单词，赋值给words
    words = stuff.split('')
    # 返回函数值 words
    return words
# 定义函数sort words，参数words
def sort_words(words):
    # （对单词进行排序）
    """Sorts the words."""
    # 返回值，调用sorted()函数对参数进行排序，并将值返回
    return sorted(words)
# 定义函数 print first word，参数words
def print_first_word(words):
    # 文档注释（弹出后打印第一个单词。）
    """Prints the first word after popping it off."""
    # words 调用函数 pop，参数 0 ，赋值给 word
    word = words.pop(0)
    # 打印参数 word
    print(word)
# 定义函数 pinrt last word，参数 words
def print_last_word(words):
    # 文档注释（弹出后输出最后一个单词。）
    """prints the last word after popping it off."""
    # words 调用函数 pop，赋值给word
    word = words.pop(-1)
    # 打印word
    print(word)
# 定义参数 sort，参数s sentense
def sort_sentence(sentence):
    # 文档注释（接受完整的句子并返回已排序的单词。）
    """Takes in a full sentence and returns the sorted words."""
    # 调用函数 break words ？？，参数 sentence，赋值给words
    words = break_words(sentence)
    # 调用函数 sort words，参数 words 并返回函数值
    return sort_words(words)
# 定义函数 print first and last，参数sentence
def print_first_and_last(sentence):
    # 文档注释（打印句子的第一个和最后一个字）
    """Prints the first and last words of the sentence."""
    # 调用函数 break words，参数 sentence，赋值给words
    words = break_words(sentence)
    # 调用函数 print first word，参数words
    print_first_word(words)
    # 调用函数 print last word，参数words
    print_last_word(words)
# 定义函数 print first and last sorted，参数sentence
def print_first_and_last_sorted(sentence):
    # 文档注释（对单词进行排序然后打印第一个和最后一个）
    """Sorts the words then prints the first and last one."""
    # 调用函数 sort sentence，函数sentence，赋值给words
    words = sort_sentence(sentence)
    # 调用函数 print first word，参数words
    print_first_word(words)
    # 调用函数 print last word，参数words
    print_last_word(words)
