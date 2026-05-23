import math
# Simple Calculator
a = 20
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Area of Shapes
radius = 7
circle_area = math.pi * radius ** 2
print("Circle Area:", circle_area)

length = 10
width = 5
rectangle_area = length * width
print("Rectangle Area:", rectangle_area)

base = 8
height = 6
triangle_area = 0.5 * base * height
print("Triangle Area:", triangle_area)

# Even or Odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Student Grade Percentage
score = 450
total = 500

percentage = (score / total) * 100
print("Percentage:", percentage)

# BMI Calculator
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI:", bmi)

# Power & Modulus
print(2 ** 3)
print(10 % 3)
