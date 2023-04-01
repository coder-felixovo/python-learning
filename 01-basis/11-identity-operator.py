# Identity Operator
# It is used to compare equality and, if they are the same object, the same memory location

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
