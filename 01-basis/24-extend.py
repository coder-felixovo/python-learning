# extend

# Create a `Person` class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Bill", "Gates")
x.printname()

# Create a class `Student` that extends `Person` class
class Student(Person):
  pass

x = Student("Elon", "Musk")
x.printname()

# Add __init__() for the `Student` class
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Elon", "Musk")
x.printname()

# super()
# Subclass inherits all methods and properties from its superclass
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Elon", "Musk")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcom(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Elon", "Musk", 2019)
x.welcom()