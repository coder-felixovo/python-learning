# 模块

# 导入自定义模块
import mymodule
mymodule.greeting("Steve")
print(mymodule.car)

# 导入内置模块
import platform
print(platform.system())

# dir()函数列出模块中所有函数名（或变量名）
# Show all function and variable name in module
print(dir(platform))

# 导入模块部件
from mymodule import car
print(car)
