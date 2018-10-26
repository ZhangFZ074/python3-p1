# 创建一个叫 Song 的类，第一个字母必须时大写，参数继承 objece
class Song(object):
    # 通过定义 __init__ 方法，让它接受两个参数，__init__方法第一个参数永远时 self
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # 定义函数 sing me dong，参数self
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# 创建类的实例
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"
                   ])
bull_on_parade = Song(["They rally around the family",
                       "with pockets full of shells"
                       ])

# 调用函数 sing me a song
happy_bday.sing_me_a_song()

bull_on_parade.sing_me_a_song()
