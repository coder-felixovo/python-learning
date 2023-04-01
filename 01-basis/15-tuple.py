# tuple
# ordered, inalterable, repeatable

thisTuple = ('a', 'b', 'c', 'a', 'd')
print(thisTuple)

# Get tuple item
print(thisTuple[1])  # "b"
print(thisTuple[-1])  # "d"

# Index range, include begin index and exclude end index
print(thisTuple[2:4])  # ('c', 'a')
print(thisTuple[-4:-1])  # ('b', 'c', 'a')

# After you create a tuple, you cannot change the item in the tuple
# thisTuple[0] = 'aaa'
# TypeError: 'tuple' object does not support item assignment

# tuple => list
# update
# list => tuple
x = ('a', 'b', 'c')
y = list(x)
y[0] = 'apple'
x = tuple(y)
print(x)  # ('apple', 'b', 'c')

# Traverse
newTuple = ('a', 'b', 'c')
for item in newTuple:
    print(item)
print('d' in newTuple)  # False
print('a' in newTuple)  # True

# Tuple length
print(len(newTuple))  # 3

# After you create a tuple, you cannot add a new item in it
myTuple = ('a', 'b', 'c')
# myTuple[3] = 'd'

# To create a tuple that contains only one item,
# you must add a comma after the item,
# or Python will not recognize variables as tuples
oneItemTuple = ("only one",)
print(type(oneItemTuple))  # <class 'tuple'>
errOneItemTuple = ("only one")
print(type(errOneItemTuple))  # <class 'str'>

# After you create a tuple, you cannot delete the item in it,
# but you can delete tuple using `del` keyword
del myTuple
# print(myTuple)
# NameError: name 'myTuple' is not defined

# Merge multiple tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
mergeTuple = tuple1 + tuple2
print(mergeTuple)  # ('a', 'b', 'c', 1, 2, 3)

# tuple() constructor
newTuple = tuple(('a', 'b', 'c'))
print(newTuple)  # ('a', 'b', 'c')



