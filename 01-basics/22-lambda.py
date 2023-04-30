# lambda 函数是一种匿名函数，可以接受任意数量参数，但只能有一个表达式
# 语法： lambda arguments : expression

x = lambda a: a + 10
print(x(5))  # 15

y = lambda x, y, z: x * y * z
print(y(3, 4, 5))  # 60

