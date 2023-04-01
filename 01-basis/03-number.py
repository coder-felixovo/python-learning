# Python has three number types: `int`, `float` and `complex`.

# int
x = 2023

# float
# Use "e" for the power of 10
y = 3.14
y2 = 3.14e2  # 314.0

# complex
# Use "j" as imaginary unit
z = 1+2j  # (1+2j)

# int => float
a = float(x)  # 2023.0

# float => int
b = int(y)  # 3

# int => complex
c = complex(x)  # (2023+0j)

# But you can't convert complex to int

# Random
import random
# A random number between 1 and 9
print((random.randrange(1, 10)))

