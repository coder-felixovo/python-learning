# if-elif-else

x, y = 10, 20
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("x is less than y")

z = 30
if y > x and z > x:
    print("y and z are more than x")

q = 5
if y > x or q > x:
    print("At least one of the conditions is True")

# Nested
v = 51
if v > 50:
    print("Above 50")
    if (v < 100):
        print("Below 50")

# pass
# The `if` statement cannot be empty,
# but if you write a content-free if statement for some reason,
# use the `pass` statement to avoid errors.
a = 100
b = 200
if b > a:
    pass