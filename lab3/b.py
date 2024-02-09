'''Python Function'''
# Python Function
# A recipe you are reading states how many grams you need for the ingredient. 
# Unfortunately, your store only sells items in ounces. Create a function to convert grams to ounces.
# ounces = 28.3495231 * grams

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = 100
result = grams_to_ounces(grams)
print(f"{grams} grams is equal to {result} ounces.")


# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade 
# temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (5 / 9) * (fahrenheit - 32)
    return centigrade

fahrenheit = float(input(""))

centigrade = fahrenheit_to_centigrade(fahrenheit)

print(f"{fahrenheit}°F is equal to {centigrade:.2f}°C.")


# Write a program to solve a classic puzzle: We count 35 heads and 94 legs 
# among the chickens and rabbits in a farm. How many rabbits and how many chickens 
# do we have? create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    for numchickens in range(numheads + 1):
        numrabbits = numheads - numchickens
        if 2*numchickens + 4*numrabbits == numlegs:
            return numchickens, numrabbits
    return "No solution"

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result[0])
print(result[1])


# You are given list of numbers separated by spaces. Write 
# a function filter_prime which will take list of numbers as an 
# agrument and returns only prime numbers from the list.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_prime(numbers)
print(result)


# Write a function that accepts string from user and print all permutations of that string.

from itertools import permutations

def print_all_permutations(user_string):
    perms = permutations(user_string)
    for perm in perms:
        print(''.join(perm))

user_input = input()

print_all_permutations(user_input)


# Write a function that accepts string from user, return a 
# sentence with the words reversed. We are ready -> ready are We

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

user_input = input()

reversed_sentence = reverse_words(user_input)

print("Reversed sentence:", reversed_sentence)


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(nums):
#     pass

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))   # True
print(has_33([1, 3, 1, 3])) # False
print(has_33([3, 1, 3]))    # False

# Write a function that takes in a list of integers and returns True if it contains 007 in order
# def spy_game(nums):
#     pass

# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False

print(spy_game([1,2,4,0,0,7,5])) # True
print(spy_game([1,0,2,4,0,5,7])) # True
print(spy_game([1,7,2,0,4,5,0])) # False


# Write a function that computes the volume of a sphere given its radius.
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

radius = 3
volume = sphere_volume(radius)
print(radius, volume)


# Write a Python function that takes a list and returns a new list
# with unique elements of the first list. Note: don't use collection set.
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_list = [1, 2, 3, 2, 4, 5, 4, 6]
result = unique_elements(input_list)
print(input_list)
print(result)

# Write a Python function that checks whether a word or phrase is 
# palindrome or not. Note: A palindrome is word, phrase, or sequence that
# reads the same backward as forward, e.g., madam
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

# Test cases
print(is_palindrome("madam"))          # True
print(is_palindrome("racecar"))        # True
print(is_palindrome("A man a plan a canal Panama")) # True
print(is_palindrome("hello"))          # False


# Define a functino histogram() that takes a list of integers and
# prints a histogram to the screen. For example, histogram([4, 9, 7]) 
# should print the following:

# ****
# *********
# *******

def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram([4, 9, 7])

# Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
# Hello! What is your name?
# KBTU

# Well, KBTU, I am thinking of a number between 1 and 20.
# Take a guess.
# 12

# Your guess is too low.
# Take a guess.
# 16

# Your guess is too low.
# Take a guess.
# 19

# Good job, KBTU! You guessed my number in 3 guesses!
import random

def guess_the_number():
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)

    guesses_taken = 0
    guess = None

    while True:
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()

# Create a python file and import some of the functions from the above 13 tasks and try to use them.
'''
from palindrome_check import is_palindrome
from unique_elements import unique_elements
from guess_the_number import guess_the_number '''

def test_functions():
  
    print("Testing is_palindrome function:")
    print(is_palindrome("madam"))          # True
    print(is_palindrome("racecar"))        # True
    print(is_palindrome("A man a plan a canal Panama")) # True
    print(is_palindrome("hello"))          # False
    print()

   
    print("Testing unique_elements function:")
    print(unique_elements([1, 2, 3, 2, 4, 5, 4, 6])) # [1, 2, 3, 4, 5, 6]
    print(unique_elements([1, 2, 2, 3, 3, 3, 4, 4, 4])) # [1, 2, 3, 4]
    print()

 
    print("Playing the 'Guess the number' game:")
    guess_the_number()

if __name__ == "__main__":
    test_functions()









'''Python Classes'''

# Python Classes
# Define a class which has at least two methods: getString: 
# to get a string from console input printString: to print 
# the string in upper case.
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())

manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

# Define a class named Shape and its subclass Square. The Square 
# class has an init function which takes a length as argument. Both 
# classes have a area function which can print the area of the 
# shape where Shape's area is 0 by default.
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print(shape.area())  # 0

square = Square(4)
print(square.area())  # 16

# Define a class named Rectangle which inherits from Shape
# class from task 2. Class instance can be constructed by 
# a length and width. The Rectangle class has a method which 
# can compute the area.
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20


# Write the definition of a Point class. Objects from this class should have a

# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show()  # (3, 4)
point2.show()  # (6, 8)

point1.move(2, 3)
point1.show()  # (5, 7)

distance = point1.dist(point2)
print(distance)  # 5.0


# Create a bank account class that has attributes owner, balance
# and two methods deposit and withdraw. Withdrawals may not 
# exceed the available balance. Instantiate your class, make 
# several deposits and withdrawals, and test to make sure the 
# account can't be overdrawn.

# class Account:
#     pass
class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount must be greater than zero.")

account = Account("John", 1000)
print(f"Initial balance for {account.owner}: {account.balance}")

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  

# Write a program which can filter prime numbers
# in a list by using filter function. Note: Use 
# lambda to define anonymous functions.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)


















'''Python Function'''

# Python Function
# # Dictionary of movies

# movies = [
# {
# "name": "Usual Suspects", 
# "imdb": 7.0,
# "category": "Thriller"
# },
# {
# "name": "Hitman",
# "imdb": 6.3,
# "category": "Action"
# },
# {
# "name": "Dark Knight",
# "imdb": 9.0,
# "category": "Adventure"
# },
# {
# "name": "The Help",
# "imdb": 8.0,
# "category": "Drama"
# },
# {
# "name": "The Choice",
# "imdb": 6.2,
# "category": "Romance"
# },
# {
# "name": "Colonia",
# "imdb": 7.4,
# "category": "Romance"
# },
# {
# "name": "Love",
# "imdb": 6.0,
# "category": "Romance"
# },
# {
# "name": "Bride Wars",
# "imdb": 5.4,
# "category": "Romance"
# },
# {
# "name": "AlphaJet",
# "imdb": 3.2,
# "category": "War"
# },
# {
# "name": "Ringing Crime",
# "imdb": 4.0,
# "category": "Crime"
# },
# {
# "name": "Joking muck",
# "imdb": 7.2,
# "category": "Comedy"
# },
# {
# "name": "What is the name",
# "imdb": 9.2,
# "category": "Suspense"
# },
# {
# "name": "Detective",
# "imdb": 7.0,
# "category": "Suspense"
# },
# {
# "name": "Exam",
# "imdb": 4.2,
# "category": "Thriller"
# },
# {
# "name": "We Two",
# "imdb": 7.2,
# "category": "Romance"
# }
# ]


# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def is_above_5_5(movie):
    return movie['imdb'] > 5.5

movie = {
    "name": "Usual Suspects", 
    "imdb": 7.0,
    "category": "Thriller"
}

print(is_above_5_5(movie))  

# Write a function that returns a sublist of movies with an IMDB score above 5.5.
def get_movies_above_5_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"}
]

print(get_movies_above_5_5(movies))


# Write a function that takes a category name and returns just those movies under that category.
def get_movies_by_category(movies, category_name):
    return [movie for movie in movies if movie['category'] == category_name]

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"}
]

category_name = "Drama"
print(get_movies_by_category(movies, category_name))




# Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb_score(movies):
    if not movies:
        return 0  
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"}
]

print(average_imdb_score(movies))


# Write a function that takes a category and computes the average IMDB score.
def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    
    if not category_movies:
        return 0 
    
    total_score = sum(movie['imdb'] for movie in category_movies)
    
    average_score = total_score / len(category_movies)
    
    return average_score

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "The Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "Inception", "imdb": 8.8, "category": "Adventure"},
    {"name": "Avengers", "imdb": 8.1, "category": "Action"}
]

category = "Adventure"
print(f"Average IMDb score for {category} movies:", average_imdb_score_by_category(movies, category))

