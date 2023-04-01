# while
i = 1
while i <= 5:
    print(i)
    i += 1

# break
# `break` statement can stop the loop even the `while` condition is true.
j = 101
while j <= 105:
    print(j)
    if j == 103:
        break
    j += 1

# continue
# stop current iteration and move on next
z = 51
while z <= 55:
    z += 1
    if z == 53:
        continue
    print(z)

# else
# When the condition is no longer true, we can run the code block once
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
