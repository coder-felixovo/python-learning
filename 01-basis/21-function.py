# Use `def` keyword to defined a function

def myFunc ():
    print("Hello from a function")
myFunc()

# param
def sayHello (name):
    print("Hello " + name)
sayHello("Bill")
sayHello("Steve")

# default param
def myFunc (sport = "running"):
    print("I like " + sport)
myFunc()
myFunc("basketball")

# param can be any data type
def printList(fruit):
    for x in fruit:
        print(x)
fruitList = ["apple", "banana", "cherry"]
printList(fruitList)

# return value
def add(x, y):
    return x + y
print(add(1, 2))

# keyword param
# The order of the parameters does not matter
def myFunc(p1, p3, p2):
    print(p1, p3, p2)
myFunc(p2="Xiaomi", p1="Huawei", p3="VIVO")

# any param
# If you don't know how many arguments will be passed to function,
# add `*` before the parameter name of the function definition.
def myFunction(*person):
    print(type(person))  # tuple
    print(person)
myFunction("John", "Merry", "Jennifer", "Rory")

# pass
# The function definition cannot be null, if null, use `pass` to avoid error
def myFunc():
    pass