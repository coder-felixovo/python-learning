# try except
try:
    print(x)
except:
    print("An exception occured")

# Multiple exceptions
try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("Something went wrong")


try:
    print("No exception")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The `try except` is finished")

# Use `raise` keyword to throw exception
x = 'hello'
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except TypeError:
    print("Something went wrong")
