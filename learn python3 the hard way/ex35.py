from sys import exit  # sys.exit 用于结束游戏
# 进入黄金房间
def gold_room():   # 定义函数 gold room
    print("This room is full of gold. How much do you take?")
    # 用户输入的内容赋值给变量 choice
    choice = input(">")
    # 这个是否可以这么理解，如果 0 在 choice 之内，或， 1 在 choice 之内
    # 如果输入不包含 0 或 1 则死
    if "0" in choice or "1" in choice:
         # 调用 int()函数，将变量 choice 的值转换为整型，并赋值给变量 how_much
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
# 进入狗熊的房间
def bear_room():
    print("Tere is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
     # 判断布尔表达式的真假,如果为 True,则一直循环直到表达式为False为止
    while True:
        choice = input(">")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # 从这个门进入黄金之门
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I fot no idea what that means.")
# 进入邪神之房间
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
# 惨死函数
def dead(why):
    print(why, "Good job!")
    exit(0)
# 启动函数
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
# 开始游戏
start()
