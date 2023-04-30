# while循环
i = 1
while i <= 5:
    print(i)
    i += 1
# 依次输出1 2 3 4 5

print('-----')

# 使用 break 关键字，即使 while 循环条件为真，也可以停止循环
j = 1
while j <= 5:
    print(j)
    if j == 3:
        break
    j += 1
# 依次输出1 2 3

print('-----')

# 使用 continue 关键字，停止本次循环，执行下一次
z = 1
while z <= 5:
    z += 1
    if z == 3:
        continue
    print(z)
# 依次输出2 4 5 6

print('-----')

# 使用 else 当条件不成立时执行相应代码块
i = 1
while i < 5:
    i += 1
else:
    print("i is no longer less than 5")
