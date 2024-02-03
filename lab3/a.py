# L3. 
# Python Functions

# Exercise:
# Create a function named my_function.
def my_function():
  print("Hello from a function")
  
# Exercise:
# Execute a function named my_function.
def my_function():
  print("Hello from a function")

my_function()

# Exercise:
# Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
  print(fname)
  
# Exercise:
# Let the function return the x parameter + 5.
def my_function(x):
    return x + 5

# Exercise:
# If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
  print("The youngest child is " + kids[2])
  
# Exercise:
# If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
  print("His last name is " + kid["lname"])

# Python Lambda

# Exercise:
# Create a lambda function that takes one parameter (a) and returns it.
x = lambda a : a


# Python Classes and Objects.

# Exercise:
# Create a class named MyClass:
class MyClass:
  x = 5

# Exercise:
# Create an object of MyClass called p1:
class MyClass:
    x = 5
    
    p1 = MyClass()

# Exercise:
# Use the p1 object to print the value of x:
class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

# Exercise:
# What is the correct syntax to assign a "init" function to a class?
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Python Inheritance

# Exercise:
# What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
class Student(Person):

# Exercise:
# We have used the Student class to create an object named x.
# What is the correct syntax to execute the printname method of the object x?


 class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
