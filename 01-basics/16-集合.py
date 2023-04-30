# 集合 set 是无序、无索引、没有重复成员，使用{}

# set是无序的，无法预测其显示顺序
mySet = {'a', 'b', 'c'}
print(mySet)
print(type(mySet))  # <class 'set'>

# set的长度
print(len(mySet))  # 3

# 无法通过索引访问set中的元素
# print(mySet[0])
# TypeError: 'set' object is not subscriptable

# 可以使用for循环遍历set中的元素
for item in mySet:
    print(item)

# 也可以使用 in 或 not in 关键字检查set中是否存在指定值
print('a' in mySet)  # True
print('d' in mySet)  # False

# 集合一旦创建就无法更改元素，但是可以添加新的元素

# add()方法将一个元素添加到set
mySet.add('d')
print('d' in mySet)  # True

# update()方法将多个元素添加到set
mySet.update(['e', 'f'])
print('e' in mySet)  # True
print('f' in mySet)  # True

# remove()方法删除set中的元素，如果该元素不存在，报错
mySet.remove('f')
print('f' in mySet)  # False
# mySet.remove('apple')  # KeyError

# discard()方法删除set中的元素，如果该元素不存在，不报错
mySet.discard('e')
print('e' in mySet)  # False
mySet.discard(('banana'))

# pop()方法删除set中最后一个元素，但由于set是无序的，所以无法预知删除了哪个元素
mySet.pop()
print(mySet)

# clear()方法清空set
mySet.clear()
print(mySet)  # set()

# del 关键字删除set
del mySet
# print(mySet)
# NameError: name 'mySet' is not defined

# union()方法合并两个set
set1 = {'a', 'b', 'c', 1}
set2 = {1, 2, 3, 'a'}
mergeSet = set1.union(set2)
print(mergeSet)  # {1, 2, 3, 'a', 'b', 'c'}

# update()方法将一个set中的元素放到另一个set
set1.update(set2)
print(set1)  # # {1, 2, 3, 'a', 'b', 'c'}

# union() 和 update() 都会排除重复元素

# se()构造函数创建set集合
newSet = set(('apple', 'banana'))  # 注意有两层括号
print(newSet)

# 其它set方法参考Python文档