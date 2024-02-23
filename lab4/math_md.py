'''
Python Math library 
'''
######
'''
1 Write a Python program to convert degree to radian.
Input degree: 15
Output radian: 0.261904
''' 
import math

def degree_to_radian(degrees):
    radians = math.radians(degrees)
    return radians

degrees_input = float(input("Input degree: "))
radian_output = degree_to_radian(degrees_input)
print("Output radian:", radian_output)

'''
2 Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
''' 
def trapezoid_area(height, base1, base2):
    area = (base1 + base2) * height / 2
    return area

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = trapezoid_area(height, base1, base2)

print("Expected Output:", area)

'''
3 Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
''' 
import math

def regular_polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = regular_polygon_area(num_sides, side_length)

print("The area of the polygon is:", area)

'''
4 Write a Python program to calculate the area of a parallelogram.
Length of base: 5
Height of parallelogram: 6
Expected Output: 30.0
'''
def parallelogram_area(base_length, height):
    return base_length * height

base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base_length, height)

print("Expected Output:", area)
