# L2. Python fundamentals.
# Python While Loops

# Exercise:
# Print i as long as i is less than 6.
i = 1
while i < 6:
  print(i)
  i += 1
  
# Exercise:
# Stop the loop if i is 3.
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
  
# Exercise:
# In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
# Exercise:
# Print a message once the condition is false.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  

# Python Lists

# Exercise:
# Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

# Exercise:
# Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# Exercise:
# Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Exercise:
# Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# Exercise:
# Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# Exercise:
# Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# Exercise:
# Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# Exercise:
# Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))


# Python For Loops

# Exercise:
# Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Exercise:
# In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)    


# Exercise:
# Use the range function to loop through a code set 6 times.
for x in range(6):
  print(x)
  

# Exercise:
# Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  


# Python Arrays

# Example 
# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"

# Example
# Get the value of the first array item:
x = cars[0]

# Example
# Modify the value of the first array item:
cars[0] = "Toyota"

# Example
# Return the number of elements in the cars array:
x = len(cars)

# Example
# Print each item in the cars array:
for x in cars:
  print(x)
  
# Example
# Add one more element to the cars array:
cars.append("Honda")

# Example
# Delete the second element of the cars array:
cars.pop(1)

# Example
# Delete the element that has the value "Volvo":
cars.remove("Volvo")

# Python Tuples

# Exercise:
# Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# Exercise:
# Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Exercise:
# Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# Exercise:
# Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


# Python Sets

# Exercise:
# Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
# Exercise:
# Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# Exercise:
# Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# Exercise:
# Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# Exercise:
# Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")


# Python Dictionaries

# Exercise:
# Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# Exercise:
# Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

# Exercise:
# Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"


# Exercise:
# Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

# Exercise:
# Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

