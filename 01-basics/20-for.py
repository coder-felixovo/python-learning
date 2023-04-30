# for循环用于遍历，可以遍历list、tuple、dict、set、str

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

print('-----')

text = 'Hello World'
for x in text:
    print(x)

print('-----')

# break 停止遍历
for x in fruits:
    if x == "banana":
        break
    print(x)

print('-----')

# continue 停止本次遍历，执行下一次
for x in fruits:
    if x == "banana":
        continue
    print(x)

print('-----')

# range()函数返回一个数字序列，默认从0开始，递增1，并以指定数字结束（不包括指定数字）
for x in range(5):
    print(x)
# 依次输出0 1 2 3 4

print('-----')

# 指定一个范围
# 包括 5 不包括 10
for x in range(5, 10):
    print(x)
# 依次输出5 6 7 8 9

print('-----')

# else 循环结束时执行
for x in range (3):
    print(x)
else:
    print("loop ok")

print('-----')

# 嵌套循环
adj = ["red", "big", "tasty"]
fruits = ["apple", "watermelon", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# for 语句不能为空，可以使用 pass 避免错误
for x in [1, 2, 3]:
    pass
