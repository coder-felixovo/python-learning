# A simple class and object example
# Use `class` keyword to create class
class FirstClass:
    x = 100
# Create object
obj1 = FirstClass()
print(obj1.x)

# __init__()
# The __init__() function is automatically called each time a new object is created with a class
# self
# The `self` argument is a reference to the current instance of the class and is used to access variables belonging to that class
# It doesn't have to be named `self`, but it has to be the first argument to the function
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
# update
p1.name = 19
print(p1.name)
# delete attribute
del p1.age
# print(p1.age)
# AttributeError: 'Person' object has no attribute 'age'
# delete object
del p1
# print(p1)
# NameError: name 'p1' is not defined

# The class definition cannot be empty
# You can use `pass` to avoid error
class Person:
    pass