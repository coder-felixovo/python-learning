# 身份运算符
# 比较两个对象是否具有相同的内存位置

x = 1
y = 1
z = x

print(x is y)  # True
print(x is z)  # True

x = ['apple', 'banana']
y = ['apple', 'banana']
z = x
print(x is y)  # False
print(x is z)  # True
print(x is not y)  # True
print(x is not z)  # False
