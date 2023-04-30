# Python中字符串字面量由单引号或双引号括起
str1 = 'Python'
str2 = "Hello World"
print(str1, str2)

# 可以使用三个单引号或双引号将多行字符串赋给变量
str3 = '''Python a
is b
awesome c'''
print(str3)

str3 = 'Hello World'

# Python中字符串是表示unicode字符的数组
# 可以通过方括号和索引访问指定位置的字符
print(str3[1])  # "e"

# 也可以裁剪返回一定范围的字符串
# 返回的字符串，包括开始索引，但不包括结束索引
print(str3[0:5])  # "Hello"
print(str3[-1])  # "d"
print(str3[-5:-2])  # "Wor"

# 使用 len() 函数获取字符串长度
print(len(str3))  # 11
