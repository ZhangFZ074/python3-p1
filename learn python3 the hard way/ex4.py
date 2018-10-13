# 这是运行的条件
---
cars = 100  # 有100辆汽车
space_in_car = 4.0  # 汽车有四个座位
drivers = 30  # 有30个司机
passengers = 90  # 有90名乘客
cars_not_driven = cars - drivers  # 那些司机没有开车
cars_driven = drivenrs  # 多少司机在开车
carpool_capacity = cars_driven * space_in_a_car  #  汽车的载客量
average_passengers_per_car = passengers / cars_driven  # 平均每辆汽车上有多少人

# 这是运行的结果。
---
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We havetransport",carpool_capacity,"people today.")
print("We have", passengers, "to carpooltoday.")
print("We need to put about", average_passengers_per_car, "in each car.")
