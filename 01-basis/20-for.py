# for
# The for loop is used to iterate over sequences
# e.g.: list, tuple, dict, set and string

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

text = 'Hello World'
for x in text:
    print(x)

# break
# stop loop
for x in fruits:
    if x == "banana":
        break
    print(x)

# continue
# stop current iteration and move next
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range()
# Use `range()` to return a number list,
# increments start at 0 by default
for x in range(5):
    print(x)

# include 5 and exclude 10
for x in range(5, 10):
    print(x)

# `else` in `for` loop
for x in range (3):
    print(x)
else:
    print("ok")

# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "watermelon", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# `for` is not empty, using `pass` to avoid error
for x in [1, 2, 3]:
    pass
