# Python has the following built-in data types by default
# String: `str`
# Number: `int`, `float`, `complex`
# Sequence: `list`, `tuple`, `range`
# Mapping: `dict`
# Collection: `set`, `frozenset`
# Boolean: `bool`
# Binary: `bytes`, `bytearray`, `memoryview`

# type()
# Get data type
arr = []
print(type(arr))  # list

# The data type is set when you assign a value to a variable
# Let's show you the different data types
v1 = "Hello"
print(type(v1))  # str
v2 = 2023
print(type(v2))  # int
v3 = 3.14
print(type(v3))  # float
v4 = 1j
print(type(v4))  # complex
v5 = ["apple", "banana", "coconut"]
print(type(v5))  # list
v6 = ("durian", "grape", "orange")
print(type(v6))  # tuple
v7 = range(10)
print(type(v7))  # range
v8 = {"name": "Felix", "age": 22}
print(type(v8))  # dict
v9 = {"apple", "banana", "cherry"}
print(type(v9))  # set
v10 = frozenset({"apple", "banana", "cherry"})
print(type(v10))  # frozenset
v11 = True
print(type(v11))  # bool
v12 = b"Hello"
print(type(v12))  # bytes
v13 = bytearray(10)
print(type(v13))  # bytearray
v14 = memoryview(bytes(10))
print(type(v14))  # memoryview

# Use a constructor to specify the data type
x1 = str("Hello World")
x2 = int(2023)
x3 = float(3.14)
x4 = complex(1j)
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

