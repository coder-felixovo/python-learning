# 字典 dict 是无序的、可变的、无索引的集合，用 {} 表示

myDict = {
    'brand': 'Porsche',
    'model': '911',
    'year': 1963
}
print(type(myDict))  # <class 'dict'>

# 字典长度
print(len(myDict))  # 3

# 访问字典中的项
value1 = myDict['model']
value2 = myDict.get('model')
print(value1 == value2)  # True

# 更改指定项的值
myDict['year'] = 2019
print(myDict['year'])  # 2019

print('-----')

# for循环遍历字典
for key in myDict:
    print(key)

print('-----')

# values()方法返回字典的值
for value in myDict.values():
    print(value)

print('-----')

# items()方法遍历字典的键和值
for key, value in myDict.items():
    print(key + ':', value)
print('-----')

# int 或 not in 关键字检查是否存在（不存在）指定键
print('brand' in myDict)  # True
print('color' in myDict)  # False

# 使用新的索引并为其赋值，可以将新的项添加到字典中
myDict['color'] = 'black'
print(myDict)

# pop()方法删除指定键名的项
myDict.pop('color')
print('color' in myDict)  # False
print(myDict)

# popitem()方法删除最后插入的项
# python3.7版本之前，随机删除项
myDict.popitem()
print(myDict)

# del 关键字删除指定键名的项
del myDict['model']
print(myDict)

# del 关键字删除整个字典
del myDict
# print(myDict)
# NameError: name 'myDict' is not defined

myDict = {
    'brand': 'Porsche'
}

# clear()方法清空字典
myDict.clear()
print(myDict)  # {}

# copy()方法复制字典
carDict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
copyDict = carDict.copy()
copyDict['year'] = '2019'
print(carDict)
print(copyDict)

# dict()方法创建字典副本
carDict = {
    'brand': 'Porsche',
    'model': 'Panamera',
}
copyDict = dict(carDict)
copyDict['model'] = 'cayman'
print(carDict)
print(copyDict)

# 字典嵌套
car718 = {
    'brand': 'Porsche',
    'model': '718'
}
car911 = {
    'brand': 'Porsche',
    'model': '911'
}
carPanamera = {
    'brand': 'Porsche',
    'model': 'Panamera'
}
carFamily = {
    'car718': car718,
    'car911': car911,
    'carPanamera': carPanamera
}
print(carFamily)

# dict()构造函数创建字典
newDict = dict(brand='Porsche', model='911', year=1963)
# 键不是字符串字面量
# 使用 = 赋值
print(newDict)

# 字典其它方法参考Python文档


