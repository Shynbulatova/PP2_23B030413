#L1. Python fundamentals.
#Python Intro
print("Hello, World!")

#Python User Input
''' PS C:\Users\Айдана\OneDrive\Desktop\python.pp2\1lab.py> python 1a.py '''
#Python Get Started

#Python Syntax
# Exercise 1:
# Insert the missing part of the code below to output "Hello World".

print("Hello World")

# Exercise 2:
# Complete the code block, print "YES" if 5 is larger than 2.

# Hint: remember the indentation.


if 5 > 2:
    print("YES")

#Python Comments

# Exercise:
# Comments in Python are written with a special character, which one?


# "#" This is a comment

# Exercise:
# Use a multiline string to make the a multiline comment:


'''

This is a comment
written in 
more than just one line
'''

#Python Variables
# Exercise:
# Create a variable named carname and assign the value Volvo to it.

carname= "Volvo"

# Exercise:
# Create a variable named x and assign the value 50 to it.

x= 50

# Exercise:
# Display the sum of 5 + 10, using two variables: x and y.


x = 5
y = 10
print(x + y)

# Exercise:
# Create a variable called z, assign x + y to it, and display the result.


x = 5
y = 10
z = x + y
print(z)

# Exercise:
# Insert the correct syntax to assign values to multiple variables in one line:


x, y, z = "Orange", "Banana", "Cherry"

# Exercise:
# Insert the correct syntax to assign the same value to all three variables in one code line.


x = y = z = "Orange"

# Exercise:
# Insert the correct keyword to make the variable x belong to the global scope.


def myfunc():
  
  global x
x = "fantastic"

#Python Data Types

# Exercise:
# The following code example would print the data type of x, what data type would that be?


x = 5
print(type(x))

int

#  Exercise:
# The following code example would print the data type of x, what data type would that be?


x = "Hello World"
print(type(x))

str

# Exercise:
# The following code example would print the data type of x, what data type would that be?


x = 20.5
print(type(x))

float

# Exercise:
# The following code example would print the data type of x, what data type would that be?


x = ["apple", "banana", "cherry"]
print(type(x))

list

# Exercise:
# The following code example would print the data type of x, what data type would that be?


x = ("apple", "banana", "cherry")
print(type(x))

tuple

# Exercise:
# The following code example would print the data type of x, what data type would that be?


x = {"name" : "John", "age" : 36}
print(type(x))

dict

# Exercise:
# The following code example would print the data type of x, what data type would that be?


x = True
print(type(x))

bool


#Python Numbers
# Exercise:
# Insert the correct syntax to convert x into a floating point number.


x = 5
x = float(x)

# Exercise:
# Insert the correct syntax to convert x into a integer.


x = 5.5
x = int(x)

# Exercise:
# Insert the correct syntax to convert x into a complex number.


x = 5
x = complex(x)


#Python Casting

#Python Strings
# Exercise:
# Use the len function to print the length of the string.


x = "Hello World"
print(len(x))

# Exercise:
# Get the first character of the string txt.


txt = "Hello World"
x = txt[0]

# Exercise:
# Get the characters from index 2 to index 4 (llo).


txt = "Hello World"
x = txt[2:5]

# Exercise:
# Return the string without any whitespace at the beginning or the end.


txt = " Hello World "
x = txt.strip()

# Exercise:
# Convert the value of txt to upper case.


txt = "Hello World"
txt = txt.upper()

# Exercise:
# Convert the value of txt to lower case.


txt = "Hello World"
txt = txt.lower()


# Exercise:
# Replace the character H with a J.


txt = "Hello World"
txt = txt.replace("H", "J")

# Exercise:
# Insert the correct syntax to add a placeholder for the age parameter.


age = 36
txt = "My name is John, and I am {}" 
print(txt.format(age))

#Python String Formatting
#Python Booleans
# Exercise:
# The statement below would print a Boolean value, which one?


print(10 > 9)

True

# Exercise:
# The statement below would print a Boolean value, which one?


print(10 == 9)

False

# Exercise:
# The statement below would print a Boolean value, which one?


print(10 < 9)

False

# Exercise:
# The statement below would print a Boolean value, which one?


print(bool("abc"))

True

# Exercise:
# The statement below would print a Boolean value, which one?


print(bool(0))

False


#Python Operators
# Exercise:
# Multiply 10 with 5, and print the result.


print(10 * 5)

# Exercise:
# Divide 10 by 2, and print the result.


print(10 / 2)

# Exercise:
# Use the correct membership operator to check if "apple" is present in the fruits object.


fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
# Exercise:
# Use the correct comparison operator to check if 5 is not equal to 10.


if 5 != 10:
  print("5 and 10 is not equal")
  
# Exercise:
# Use the correct logical operator to check if at least one of two statements is True.


if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


#Python If...Else
# Exercise:
# Print "Hello World" if a is greater than b.


a = 50
b = 10
if a > b:
   print("Hello World")
   
# Exercise:
# Print "Hello World" if a is not equal to b.


a = 50
b = 10
if a != b:

  print("Hello World")
  
# Exercise:
# Print "Yes" if a is equal to b, otherwise print "No".


a = 50
b = 10
if a == b:

  print("Yes")
else:

  print("No")
  
# Exercise:
# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".


a = 50
b = 10
if a == b:

  print("1")
elif a > b:

  print("2")
else:

  print("3")
  
# Exercise:
# Print "Hello" if a is equal to b, and c is equal to d.


if a == b and c == d:
  print("Hello")
  
# Exercise:
# Print "Hello" if a is equal to b, or if c is equal to d.


if a == b or c == d:
  print("Hello")
  
# Exercise:
# Complete the code block, print "YES" if 5 is larger than 2.

# Hint: remember the indentation.


if 5 > 2:
    print("YES")


# Exercise:
# Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").


a = 2
b = 5

if a == b :
    print("YES") 
else : 
    print("NO")
 
 
# Exercise:
# Use an if statement to print "YES" if either a or b is equal to c.


a = 2
b = 50
c = 2
if a == c or b == c:

  print("YES")
#Git
