# Python中有4种集合数据类型
# 列表 list 有序、可更改、允许重复成员
# 元组 tuple 有序、不可更改、允许重复成员
# 集合 set 无序、无索引、没有重复成员
# 词典 dict 无序、可变、有索引、没有重复成员


# 列表 list 用 [] 表示
fruitList = ['apple', 'banana', 'cherry', 'orange', 'mango']
print(fruitList)

# 列表长度
print(len(fruitList))  # 5

# 通过索引访问列表项
print(fruitList[0])  # "apple"
print(fruitList[-1])  # "mango"

# 指定索引范围返回新列表，包括开始索引，不包括结束索引
print(fruitList[0: 2])  # ['apple', 'banana']
print(fruitList[-3: -1])  # ['cherry', 'orange']

# 使用索引更改列表项的值
fruitList[0] = 'apple-update'

# for循环遍历列表
for item in fruitList:
    print(item)

# 检查列表是否存在指定列表项
if "apple" in fruitList:
    print("Yes, 'apple' is in the fruitList")
else:
    print("'apple' is not in the fruitList")

# append()方法将列表项添加到列表末尾
fruitList.append('strawberry')
print(fruitList)

# insert()方法在指定索引处添加列表项
fruitList.insert(1, 'coconut')
print(fruitList)

# remove()删除指定列表项
fruitList.remove('apple-update')
print(fruitList)

# pop()删除指定索引，未指定索引则删除最后一箱
fruitList.pop()
print(fruitList)
fruitList.pop(1)
print(fruitList)

# del关键字删除指定索引
del fruitList[0]
print(fruitList)
# 也能完整地删除列表
del fruitList

# clear()方法清空列表
fruitList = ['apple', 'banana']
fruitList.clear()
print(fruitList)  # []

# copy()方法复制列表
a = ['apple', 'banana']
b = a.copy()
b[0] = 'a'
print(a)
print(b)
# a和b互不影响

# list()方法复制列表
a2 = ['hello', 'world']
b2 = list(a2)
b2[0] = 'hi'
print(a2)
print(b2)
# a2和b2互不影响

# 合并列表
# 1. 使用 + 运算符
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
mergeList = list1 + list2
print(mergeList)

# 2. 遍历，append()
list3 = [1, 2, 3]
list4 = [4, 5, 6]
for item in list4:
    list3.append((item))
print(list3)

# 3. extend()方法将一个列表中的元素添加到另一个列表
list5 = [-1, -2, -3]
list6 = [-4, -5, -6]
list5.extend(list6)
print(list5)

# list()构造函数创建一个新的列表
newList = list(('apple', 'banana', 'cherry'))  # 注意这里有两层括号
print(newList)
print(type(newList))  # <class 'list'>

# 其它list方法参考Python文档






