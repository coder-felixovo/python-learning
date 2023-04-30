# 作用域

def myFn1():
    x = 100  # 局部变量
    print(x)
myFn1()

y = 200  # 全局变量

def myFn2():
    print(y)
myFn2()

z = 300

def myFn3():
    z = 400
    print(z)
myFn3()

# 在函数内使用 global 关键字定义全局变量
def myFn4():
    global foo
    foo = 1
myFn4()
print(foo)

# 在函数内使用 global 关键字修改全局变量的值
bar = 1
def myFn5():
    global bar
    bar = 100
myFn5()
print(bar)


