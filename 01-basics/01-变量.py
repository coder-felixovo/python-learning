# python没有声明变量的命令
# 首次为变量赋值时，才会创建变量
x = 1
y = "apple"
print(x, y)

# 变量不需要类型声明，可以在赋值后更改其类型
x = "banana"
y = 2
print(x, y)

# 字符串变量可以使用单引号或双引号
z = 'coconut'
z = "cherry"

# 变量命名规则
# 1. 变量名必需以字母或下划线字符开头
# 2. 变量名不能以数字开头
# 3. 变量名智能包含字母、数字字符和下划线，即0-9，a-z，A-Z，_
# 4. 变量名区分大小写

# 允许在一行为多个变量赋值
a, b, c = "apple", "banana", "cherry"
print(a, b, c)
# 也可以在一行为多个变量赋相同的值
d = e = f = "Python"
print(d, e, f)

# print()通常用于输出变量，可以用 + 结合文本和变量
year = "2023"
print("year is: " + year)
# 注意，如果year是数字2023，那么上面一行语句将会报错

# 对于数字，+ 用作数学运算符
x1 = 1
x2 = 99
print(x1 + x2)

# 如果尝试使用 + 组合数字和字符串，会报错
year = 2023
# print("year: " + year) # Error

# 在函数外部创建的变量称为全局变量（上面的变量均为全局变量）
# 全局变量可以在函数内部和外部被使用
foo = "awesome"
def myFunc1 ():
    print("Python is " + foo)
myFunc1()

# 如果在函数内部创建具有与全局变量相同名称的变量，那么该变量是局部变量，并且只能在函数内部使用
# 具有相同名称的全局变量将拥有原始值
bar = 'awesome'
def myFunc2():
    bar = 'fantastic'
    print("Python is " + bar)
myFunc2()
print("bar is " + bar)

# 可以使用 global 关键字在函数内部创建全局变量
def myFunc3():
    global baz
    baz = "wonderful"
myFunc3()
print("baz is " + baz)

# 在函数内部，也可以使用 global 关键字来更改全局变量
bax = "beautiful"
def myFunc4():
    global bax
    bax = "pretty"
myFunc4()
print("The girl is " + bax)