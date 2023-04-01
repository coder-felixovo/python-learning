# lambda
# lambda functions are anonymous functions that can take any number of arguments, but only one expression

# Syntax
# lambda arguments : expression

x = lambda a: a + 10
print(x(5))  # 15

y = lambda x, y, z: x * y * z
print(y(3, 4, 5))  # 60

