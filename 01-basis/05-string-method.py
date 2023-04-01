# Use strip() to remove whitespace characters from the beginning and end of strings
str1 = ' Hello World '
print(str1.strip())  # "Hello World"

# Use lower() to return lowercase string
str2 = 'Hello World'
print(str2.lower())  # "hello world"

# Use upper() to return uppercase string
print(str2.upper())  # "HELLO WORLD"

# Use replace() to replace the original string with another string
print(str2.replace('World', 'Python'))  # "Hello Python"

# Use split() to split the string through the separator
str3 = "C, C++, Java, Python"
print(str3.split(','))  # ['C', ' C++', ' Java', ' Python']

# Use the `in` or `not int` keyword to check whether the specified string exists in the string
txt = "China is a great country"
print('China' in txt)  # True
print('b' in txt)  # False

# String cascade
a = 'Hello'
b = 'World'
print(a + " " + b)  # "Hello World"

# Use format() to combine string and number
year = 2023
txt = 'This year is {}'
print(txt.format(year))  # "This year is 2023"

# Use indexes to ensure that parameters are placed in the correct location
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Named index
quantity = 3
itemno = 567
price = 49.95
myorder = f"I want to pay {price} dollars for {quantity} pieces of item {itemno}."
print(myorder.format(quantity, itemno, price))
