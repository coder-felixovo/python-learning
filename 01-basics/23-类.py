# Python也是一种面向对象编程语言，Python中几乎所有东西都是对象，拥有属性和方法

# 使用 class 关键字定义类
class FirstClass:
    x = 100  # 属性
# 创建对象
obj1 = FirstClass()
print(obj1.x)

# 所有类都有一个名为　__init__()　的函数，它始终在启动类时执行
# 该函数将值赋给对象的属性，或者在创建对象时需要执行其它操作
# 每次使用类创建对象，都会自动调用该函数
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("Hello, my name is " + self.name)
p1 = Person("Jennifer", 18)
print(p1.name)
print(p1.age)
p1.introduce()

# 修改对象属性
p1.age = 19
print(p1.age)

# 删除对象属性
del p1.age
# print(p1.age)
# AttributeError: 'Person' object has no attribute 'age'

# 删除对象
del p1
# print(p1)
# NameError: name 'p1' is not defined

# 类定义不能为空，可以使用 pass 避免错误
class Person:
    pass