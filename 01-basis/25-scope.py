# scope

def myFn1():
    x = 100  # x is a local variable
    print(x)
myFn1()

y = 200  # y is global varibale

def myFn2():
    print(y)
myFn2()

z = 300

def myFn3():
    z = 400
    print(z)
myFn3()

# Use `global` keyword to create a global variable in function
def myFn4():
    global foo
    foo = 1
myFn4()
print(foo)

# Use `global` keyword to update a global variable in function
bar = 1
def myFn5():
    global bar
    bar = 100
myFn5()
print(bar)


