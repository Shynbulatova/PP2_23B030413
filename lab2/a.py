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
    

# Python Arrays
# Python Tuples
# Python Sets
# Python Dictionaries
