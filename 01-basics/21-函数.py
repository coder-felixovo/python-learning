# 使用 def 关键字定义函数

# 定义函数
def myFunc ():
    print("Hello from a function")
# 调用函数
myFunc()

# 参数
def sayHello (name):
    print("Hello " + name)
sayHello("Python")

# 默认参数
def myFunc (sport = "running"):
    print("I like " + sport)
myFunc()
myFunc("basketball")

# 参数可以是任何数据类型
def printList(fruit):
    for x in fruit:
        print(x)
fruitList = ["apple", "banana", "cherry"]
printList(fruitList)

# 返回值
def add(x, y):
    return x + y
print(add(1, 2))

# 关键字参数
# 调用函数传参时，参数顺序不影响
def myFunc(p1, p3, p2):
    print(p1, p3, p2)
myFunc(p2="Xiaomi", p1="Huawei", p3="VIVO")

# 任意参数
# 不知道要传多少个参数时，在函数定义的参数名称加 * ，函数将接收一个参数元组
def myFunction(*person):
    print(type(person))  # <class 'tuple'>
    print(person)
myFunction("John", "Merry", "Jennifer", "Rory")

# 函数定义不能为空，可以使用 pass 避免错误
def myFunc():
    pass