# Python 有以下内置数据类型
# 字符串类型：str
# 数值类型：int，float，complex
# 序列类型: list，tuple，range
# 映射类型：dict
# 集合类型：set，frozenset
# 布尔类型：bool
# 二进制类型：bytes，bytearray，memoryview

# 可以使用 type() 函数获取数据类型

# 当为变量赋值时，会设置相应的数据类型
v1 = "Python"
print(type(v1))  # <class 'str'>

v2 = 2023
print(type(v2))  # <class 'int'>

v3 = 3.14
print(type(v3))  # <class 'float'>

v4 = 1 + 2j
print(type(v4))  # <class 'complex'>

v5 = ["apple", "banana", "coconut"]
print(type(v5))  # <class 'list'>

v6 = ("durian", "grape", "orange")
print(type(v6))  # <class 'tuple'>

v7 = range(10)
print(type(v7))  # <class 'range'>

v8 = {"name": "Felix", "age": 22}
print(type(v8))  # <class 'dict'>

v9 = {"apple", "banana", "cherry"}
print(type(v9))  # <class 'set'>

v10 = frozenset({"apple", "banana", "cherry"})
print(type(v10))  # <class 'frozenset'>

v11 = True
print(type(v11))  # <class 'bool'>

v12 = b"Hello"
print(type(v12))  # <class 'bytes'>

v13 = bytearray(10)
print(type(v13))  # <class 'bytearray'>

v14 = memoryview(bytes(10))
print(type(v14))  # <class 'memoryview'>

# 使用构造函数指定数据类型
x1 = str("Python")
x2 = int(2023)
x3 = float(3.14)
x4 = complex(1 + 2j)
x5 = list(["apple", "banana", "cherry"])
x6 = tuple(("apple", "banana", "cherry"))
x7 = range(10)
x8 = dict(name="Felix", age=22)
x9 = set(("apple", "banana", "cherry"))
x10 = frozenset(("apple", "banana", "cherry"))
x11 = bool(5)
x12 = bytes(1)
x13 = bytearray(1)
x14 = memoryview(bytes(1))

