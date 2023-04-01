# Set
# unordered, no index, nonredundant

mySet = {'a', 'b', 'c'}
print(mySet)
# Set is unordered, so you cannot determine the order in which item should be displayed.

# Set has no index, so items cannot be accessed through an index.
# print(mySet[0])
# TypeError: 'set' object is not subscriptable

# Traverse
for item in mySet:
    print(item)

print('a' in mySet)  # True
print('d' in mySet)  # False

# update ×
# add √

# add()
# Adds an item to set
mySet.add('d')
print('d' in mySet)  # True

# update()
# Adds multiple items
mySet.update(['e', 'f'])
print('e' in mySet)  # True
print('f' in mySet)  # True

# Set length
print(len(mySet))

# remove()
# Deletes an item from a Set
mySet.remove('f')
print('f' in mySet)  # False
# If item is not in Set, error
# mySet.remove('apple')

# discard()
# Deletes an item from a Set
mySet.discard('e')
print('e' in mySet)  # False
# If item is not in Set, no error will be thrown
mySet.discard(('banana'))

# You can also use `pop()` to delete item,
# it will delete the last item,
# but Set is unordered, you couldn't predict which item to delete
mySet.pop()
print(mySet)

# clear()
# Clear Set
mySet.clear()
print(mySet)  # set()

# del
# Delete Set
del mySet
# print(mySet)
# NameError: name 'mySet' is not defined

# Merge set
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3, 'a'}
mergeSet = set1.union(set2)
print(mergeSet)  # {1, 2, 3, 'a', 'b', 'c'}

set1.update(set2)
print(set1)  # # {1, 2, 3, 'a', 'b', 'c'}

# union() and update() will remove duplicates.

newSet = set(('apple', 'banana'))
print(newSet)
