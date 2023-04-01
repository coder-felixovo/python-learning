# Python has no command to declare variabels
# A variable is created when it is first assigned
x = 1
y = "apple"
print(x, type(x))
print(y, type(y))

# Variables do not required a specific type declaration
# It can even be changed after the assignment
x = "banana"
y = 2
print(x, type(x))
print(y, type(y))

# String variables can use single or double quotes
z = 'zoo'
# is the same as
z = "zoo"

# Variables naming rule
# 1. Variable names must begin with a letter or an underscore
# 2. Variable names cannot begin with a number
# 3. Variable names can contain only alphanumeric characters and underscores
# 4. Variable names are case sensitive

# Python allows you to assign values to multiple variables on a single line
a, b, c = "apple", "banana", "coconut"
print(a, b, c)
# You can also assign the same value to multiple variables in a row
d = e = f = "same"
print(d, e, f)

# Print the variable by using the print function
# Use "+" to combine text an variables
year = "2023"
print("year: " + year)

# For numbers, "+" acts as a mathematical operator
x1 = 1
x2 = 99
print(x1 + x2)

# If you use "+" to combine a string and a number, python gives you an error
year = 2023
# print("year: " + year) # Error

# Variables created outside a function are called global variables
# All of the above examples are global variables
# Global variables can be used both outside and inside functions
foo = "awesome"
def myFunc1 ():
    print("Python is " + foo)
myFunc1()

# If a variable with the same name as a global variable is created inside a function,
# the variable is local and can only be used inside the function.
# Global variables with the same name are retained
bar = 'awesome'
def myFunc2():
    bar = 'fantastic'
    print("Python is " + bar)
myFunc2()
print("bar is " + bar)

# You can use the global keyword to create global variables inside a function
def myFunc3():
    global baz
    baz = "wonderful"
myFunc3()
print("baz is " + baz)

# You also can change global variables within a function by using the global keyword
bax = "beautiful"
def myFunc4():
    global bax
    bax = "pretty"
myFunc4()
print("The girl is " + bax)