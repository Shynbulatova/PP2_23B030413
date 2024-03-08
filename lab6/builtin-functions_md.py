# Python builtin functions exercises
# Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce

def multiply_list(numbers):
    result = reduce(lambda x, y: x * y, numbers)
    return result

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print(result)



# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = input("Enter a string: ")
upper, lower = count_upper_lower(input_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)



# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(string):
    clean_string = ''.join(char.lower() for char in string if char.isalnum())
    return clean_string == clean_string[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



# Write a Python program that invoke square root function after specific milliseconds.

# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858
import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result

number = int(input("Enter a number: "))
milliseconds = int(input("Enter milliseconds: "))

sqrt_result = delayed_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {sqrt_result}")



# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t):
    return all(t)

my_tuple = (True, True, True)
print(all_true(my_tuple))

my_tuple = (True, False, True)
print(all_true(my_tuple))