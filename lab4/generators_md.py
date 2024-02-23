
# Python iterators and generators
# Create a generator that generates the squares of numbers up to some number N.
def squares_generator(N):
    for i in range(1, N+1):
        yield i*i

N = 5
squares = squares_generator(N)
for square in squares:
    print(square)



# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers_generator(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

def main():
    try:
        n = int(input("Enter a number (n): "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        
        even_nums = even_numbers_generator(n)
        print("Even numbers between 0 and", n, "are:", end=" ")
        print(*even_nums, sep=", ")

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()


# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4_generator(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

def main():
    try:
        n = int(input("Enter a number (n): "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")

        divisible_nums = divisible_by_3_and_4_generator(n)
        print("Numbers divisible by both 3 and 4 between 0 and", n, "are:", end=" ")
        print(*divisible_nums, sep=", ")

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()


# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for num in range(a, b + 1):
        yield num * num

a = 3
b = 7

print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)


# Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test the generator with a for loop
n = 5

print(f"Counting down from {n} to 0:")
for num in countdown(n):
    print(num)
