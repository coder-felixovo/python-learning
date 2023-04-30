# 条件语句
# if、elif、else

x, y, z = 10, 20, 30

if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
else:
    print("x is less than y")

# 使用 and 关键字
if y > x and z > x:
    print("y and z are more than x")

# 使用 or 关键字
q = 1
if y > x or q > x:
    print("At least one of the conditions is True")

# 嵌套
v = 51
if v > 50:
    print("Above 50")
    if (v < 100):
        print("Below 50")

# if 语句不能为空，如果因为某种原因写出无内容的 if 语句，使用 pass 来避免错误
a = 100
b = 200
if b > a:
    pass