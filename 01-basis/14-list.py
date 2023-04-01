# List
# ordered、modifiable、repeatable member

fruitList = ['apple', 'banana', 'cherry', 'orange', 'mango']
# print(fruitList)

# Access list item through index
print(fruitList[0])  # "apple"
print(fruitList[-1])  # "mango"

# Specified index range
# Exclude end index
print(fruitList[0: 2])  # ['apple', 'banana']
print(fruitList[-3: -1])  # ['cherry', 'orange']

fruitList[0] = 'apple-update'

for item in fruitList:
    print(item)

if "apple" in fruitList:
    print("Yes, 'apple' is in the fruitList")
else:
    print("'apple' is not in the fruitList")

print(len(fruitList))  # 5

# Add to end
fruitList.append('strawberry')
print(fruitList)

# Insert to the specified position
fruitList.insert(1, 'coconut')
print(fruitList)

# Delete specified list item
fruitList.remove('apple-update')
print(fruitList)

# pop()
# Delete specified index, if not, delete the last item
fruitList.pop()
print(fruitList)

# del keyword
# Delete specified index
del fruitList[0]
print(fruitList)
# Delete list
del fruitList

# clear()
# Clear list
fruitList = ['apple', 'banana']
fruitList.clear()
print(fruitList)  # []

# copy()
a = ['apple', 'banana']
b = a.copy()
b[0] = 'a'
print(a)
print(b)

# list()
a2 = ['hello', 'world']
b2 = list(a2)
b2[0] = 'hi'
print(a2)
print(b2)

# Merge multiple lists
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
# 1.
# mergeList = list1 + list2
# 2.
# for item in list2:
#     list1.append((item))
# 3.
# list1.extend(list2)
# print(list1)

# list() constructor
newList = list(('a', 'b', 'c'))
print(newList)






