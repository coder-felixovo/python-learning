print(1 == 1)  # True
print(1 == 2)  # False

# True for any string except the empty string
print(bool('Hello'))  # True

# True for any number except 0
print(bool(1))  # True

print('-----')

# True for any list, tuple, set and dict, except empty
print(bool([1]))  # True
print(bool((2)))  # True
print(bool({3}))  # True
print(bool({'four': 4}))  # True

print('-----')

# Return False
print(bool(''))
print(bool(0))
print(bool(None))
print(bool(False))
print(bool([]))
print(bool(()))
print(bool({}))