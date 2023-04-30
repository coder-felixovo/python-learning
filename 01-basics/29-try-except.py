# try except
try:
    print(x)
except:
    print("An exception occured")

print('-----')

# 多个异常
try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("Something went wrong")

print('-----')

try:
    print("No exception")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print('-----')

# finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The `try except` is finished")

print('-----')

# 使用 raise 关键字抛出异常
x = 'hello'
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except TypeError:
    print("Something went wrong")
