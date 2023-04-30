# strip() 方法删除开头和结尾的空白字符
str1 = ' Hello World '
print(str1)  # " Hello World "
print(str1.strip())  # "Hello World"

# lower() 方法返回小写字符串
str2 = 'Hello World'
print(str2.lower())  # "hello world"

# upper() 方法返回大写字符串
print(str2.upper())  # "HELLO WORLD"

# replace() 方法用另一段字符串来替换字符串，不改变原字符串
print(str2.replace('World', 'Python'))  # "Hello Python"
print(str2)

# split() 方法使用分隔符将字符串拆分为子字符串，返回一个list
str3 = "C, C++, Java, Python"
print(str3.split(','))  # ['C', ' C++', 'Java', 'Python']

# in 或 not in 关键字检查字符串中是否包含（不包含）给定字符串
txt = "China is a great country"
print('China' in txt)  # True
print('America' in txt)  # False

# + 运算符连接字符串
a = 'Hello'
b = 'Python'
print(a + " " + b)  # "Hello Python"

# format() 方法可以组合字符串和数字，接受传递的参数（不限个数），并放在 {} 占位符中
year = 2023
txt = 'This year is {}'
print(txt.format(year))  # "This year is 2023"

# 使用索引号确保参数被放在正确的位置
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# 也可以使用参数名来占位
quantity = 3
itemno = 567
price = 49.95
myorder = f"I want to pay {price} dollars for {quantity} pieces of item {itemno}."
print(myorder.format(quantity, itemno, price))

# 其它方法参考Python文档
