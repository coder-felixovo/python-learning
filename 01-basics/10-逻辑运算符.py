# 逻辑运算符
# and 两个表达式都为真，则返回true
# or 其中一个表达式为真，则返回true
# not 取反

x = 1
y = 2
z = True

r1 = x > y and x < y
r2 = x > y or x < y
r3 = not z

print(r1)  # False
print(r2)  # True
print(r3)  # False