# 元组 tuple 是有序、不可更改、允许重复成员的集合，使用()

# 使用()
thisTuple = ('a', 'b', 'c', 'a', 'd')
print(thisTuple)

# 元组长度
print(len(thisTuple))  # 5

# 访问元组项
print(thisTuple[1])  # b
print(thisTuple[-1])  # d

# 使用索引范围返回指定元组项的新元组
print(thisTuple[2:4])  # ('c', 'a')
print(thisTuple[-4:-1])  # ('b', 'c', 'a')

# 创建元组后，元组中的值是不可改变的
# thisTuple[0] = 'aaa'
# TypeError: 'tuple' object does not support item assignment

# 解决方法
# 先将tuple => list，修改，然后list => tuple
x = ('a', 'b', 'c')
y = list(x)
y[0] = 'apple'
x = tuple(y)
print(x)  # ('apple', 'b', 'c')

# for循环遍历元组
newTuple = ('a', 'b', 'c')
for item in newTuple:
    print(item)
print('d' in newTuple)  # False
print('a' in newTuple)  # True


# 元组一旦创建，是不可改变的，因此也无法新添加项目
myTuple = ('a', 'b', 'c')
# myTuple[3] = 'd'

# 如果创建只有一个元素的元组，必需在后面添加一个逗号，否则无法识别为元组
oneItemTuple = ("only one",)
print(type(oneItemTuple))  # <class 'tuple'>
errOneItemTuple = ("only one")
print(type(errOneItemTuple))  # <class 'str'>

# 元组一旦创建，是不可更改的，因此无法删除元组项目
# del myTuple[0]  # TypeError

# 但是可以使用 del 关键字完全删除元组
del myTuple
# print(myTuple)
# NameError: name 'myTuple' is not defined

# 使用 + 运算符合并两个元组
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
mergeTuple = tuple1 + tuple2
print(mergeTuple)  # ('a', 'b', 'c', 1, 2, 3)

# 使用 tuple() 构造函数创建元组
newTuple = tuple(('a', 'b', 'c'))  # 注意有两层括号
print(newTuple)  # ('a', 'b', 'c')



