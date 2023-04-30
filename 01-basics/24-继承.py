# 继承

# 创建父类
class Animal:
  def __init__(self, type, name):
    self.type = type
    self.name = name

  def printname(self):
    print(self.type, self.name)

x = Animal("Dog", "Huskie")
x.printname()

# 创建子类
class Cat(Animal):
  pass

x = Cat("Cat", "orange cat")
x.printname()

# 手动添加 __init__() 函数
# 子类将不再继承父类的 __init__() 函数，子类的会覆盖父类的
# 如果需要对父类的 __init__() 函数继承，则添加对父类的 __init__() 函数调用
class Panda(Animal):
  def __init__(self, type, name):
    Animal.__init__(self, type, name)

x = Panda("Bear", "panda")
x.printname()

# super()函数，使子类继承父类所有的属性和方法
class Tiger(Animal):
  def __init__(self, type, name):
    super().__init__(type, name)

x = Tiger("Tiger", "south china tiger")
x.printname()