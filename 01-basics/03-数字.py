# Python有3种数字类型：int、float、complex

# int 整数
x1 = 1
x2 = -1
print(x1, x2)  # 1 -1

# float 浮点数
# 使用 e 表示科学计数法
y1 = 3.14
y2 = 3.14e2  # 314.0
print(y1, y2)  # 3.14 314.0

# complex 复数
# 使用 j 表示复数的虚部编写
z1 = 1 + 2j
print(z1)  # (1+2j)

# int => float
a = float(x1)
print(a)  # 1.0

# float => int
b = int(y1)
print(b)  # 3

# int => complex
c = complex(x1)
print(c)  # (1+0j)

# 无法将复数转换为其它数字类型

# 随机数
import random
print((random.randrange(1, 10)))  # 1 ~ 9之间的随机数

