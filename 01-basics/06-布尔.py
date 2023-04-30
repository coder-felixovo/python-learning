# 布尔值：True、False

# 通常需要知道一个表达式的布尔值
print(1 == 1)  # True
print(1 == 2)  # False

print('-----')

# bool() 函数可以评估任何值，返回True或False

# 除了空字符串，任何字符串均为True
print(bool('Hello'))  # True

# 除了0，任何数字均为True
print(bool(1))  # True

print('-----')

# 除了空列表外，任何列表、元组、集合和字典均为True
print(bool([1]))  # True
print(bool((2)))  # True
print(bool({3}))  # True
print(bool({'four': 4}))  # True

print('-----')

# 以下值均返回False
print(bool(''))
print(bool(0))
print(bool(None))
print(bool(False))
print(bool([]))
print(bool(()))
print(bool({}))

print('-----')

# Python中有很多返回布尔值的内置函数
# 例如：isinstance()函数确定对象是否是某种数据类型
test = 100
print(isinstance(test, int))  # True
print(isinstance(test, float))  # False