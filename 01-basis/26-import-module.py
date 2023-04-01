import mymodule
mymodule.greeting("Steve")
print(mymodule.car)

# build-in module
import platform
print(platform.system())

# dir()
# Show all function and variable name in module
print(dir(platform))

# Use `from` keyword to import part of module
from mymodule import car
print(car)
