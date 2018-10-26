# creat a mapping of state to abbreviation
# 创建一个字典将美国州的全称与其简称映射起来
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# creat a basic set of states and some sities in them
# 创建一个字典将美国州的简称与其中某个城市的全称映射起来
cities = {
    'CA':'San Franxisco',
    'MI':'Detroit',
    'FL':'jacksonville'
}

# add some more cities
# 在字典中增加等多的城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbrebiation is:", states['Michigan'])
print("Florida's abbrebiation is:", states['Florida'])

#doitusing the sate then cities dict
print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# print every state abbreviation
# 打印每个州的缩写
print('-' * 10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# print every city in states
# 每个州都要打印
print('-' * 10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
# 现在同事做两件
print('-' * 10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

# safely get a abbreviation by state that might not be There
# 安全得到一个可能不在那里的州的缩写
print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry,no Texas.")

# get a city with a default value
# 获取具有默认值的城市
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
