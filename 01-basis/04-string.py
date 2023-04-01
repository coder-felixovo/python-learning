# String literals are enclosed in single or double quotes
str1 = 'hello'
str2 = "hi"

# Wrap a multiline string with three double or single quotes
ms = '''Python
is
awesome'''

str3 = 'Hello World'

# A string in Python is an array of bytes representing unicode characters
# Python doesn't have a character datatype
# A single character is a string of length 1
print(str3[0])  # "H"

# Returns a part of a string
# Excludes end index
print(str3[0:5])  # "Hello"
print(str3[-1])  # "d"
print(str3[-5:-2])  # "Wor"

# string length
print(len(str3))  # 11
