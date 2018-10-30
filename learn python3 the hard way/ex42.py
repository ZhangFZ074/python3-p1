# 将每一个##？？注释替换为能说明下一行
# 是表示“is-a”（是什么）关系，还是“has-a”（有什么）关系的注释
# 并讲明白这个关系是什么
## Animal is-a object (yes, sort of confusing) look at the extra credit
# 初始类 Aniamal 继承自 object
class Aniamal(object):
    pass

## 狗是动物，Dog is-a Animal
class Dog(Aniamal):

    def __init__(self, name):
        ## 狗有一个名为 name 的属性，Dog has-a attribute named name
        self.name = name

## 猫也是动物，Cat is-a Aniamal
class Cat(Aniamal):

    def __init__(self, name):
        ## 猫有一个名为 name 的属性，Cat has-a attribute named name
        self.name = name

## 人是一个对象，Person is-a object
class Person(object):

    def __init__(self, name):
        ## 人有一个nama的属性，Person has-a attribute namad name
        self.name = name

    ## 人有宠物，Person has-a pet of some kind
        self.pet = None

## 员工是人，Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a attribute named name. hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## 员工有一个属性叫工资，Employee has-a attribute named salary
        self.salary = salary

## 初始类，fish is-a object
class Fish(object):
    pass

## 鲑鱼是鱼，Salmon is-a object
class Salmon(Fish):
    pass

## 鲽鱼是鱼，Halibut is-a Fish
class Halibut(Fish):
    pass

## 流浪是狗，rover is-a Dog
rover = Dog("Rover")

## 撒旦是猫，satan is-a Cat
satan = Cat("Santan")

## 玛丽是人，mary is-a Person
mary = Person("Mary")

## 玛丽有一只叫做 satan 额猫的宠物，mary has-a pet of Cat named Santan
mary.pet = satan

## 有一个叫 frank 的员工 他的薪水是120000，frank is-a Employee, frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank 有一只狗做宠物，Frank has-a pet of Dog maned Rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon Fish
crouse = Salmon()

## harry is-a Halibut Fish
harry = Halibut
