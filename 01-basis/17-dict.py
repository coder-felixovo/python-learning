# dict
# unordered, changeable, index, key and value

myDict = {
    'brand': 'Xiaomi',
    'model': 'Redmi K20pro',
    'price': 2199
}

# Access dict item
value1 = myDict['model']
value2 = myDict.get('model')
print(value1 == value2)  # True

# Update
myDict['price'] = 1999
print(myDict['price'])

# Traverse

print('-----')
for key in myDict:
    print(key)
print('-----')
for value in myDict.values():
    print(value)
print('-----')
for key, value in myDict.items():
    print(key + ':', value)
print('-----')

# key
print('brand' in myDict)  # True
print('color' in myDict)  # False

# dict length
print(len(myDict))

# Add
myDict['color'] = 'red'
print(myDict)

# pop()
# Delete specified key item
myDict.pop('color')
print('color' in myDict)  # False
print(myDict)

# popitem()
# Delete the last item
myDict.popitem()
print(myDict)

# del
# Delete specified key item
del myDict['model']
print(myDict)
# or delete dict
del myDict
# print(myDict)
# NameError: name 'myDict' is not defined

myDict = {
    'brand': 'Xiaomi'
}

# clear()
# Clear dict
myDict.clear()
print(myDict)  # {}

# copy()
carDict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
copyDict = carDict.copy()
copyDict['price'] = '200W'
print(carDict)
print(copyDict)

# dict()
carDict = {
    'brand': 'Porsche',
    'model': 'Panamera',
}
copyDict = dict(carDict)
copyDict['price'] = '200W'
print(carDict)
print(copyDict)

# Nested dict
car718 = {
    'brand': 'Porsche',
    'model': '718'
}
car911 = {
    'brand': 'Porsche',
    'model': '911'
}
carPanamera = {
    'brand': 'Porsche',
    'model': 'Panamera'
}
carFamily = {
    'car718': car718,
    'car911': car911,
    'carPanamera': carPanamera
}
print(carFamily)

# dict() constructor
# Use dict() to create new dict
newDict = dict(brand='Porsche', model='911', year=1963)
# key is not string literal
# Assign value using equal signs instead of colons
print(newDict)


