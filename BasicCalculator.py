import math
import numpy

print("Welcome to Basic Calculator 1.0!")
print("")
   
num1 = float(input("Enter your first number . . . "))
print("\nWhat action will you take?")
print("Valid options:\nadd , subtract, multiply, divide, square, cube, square root, cube root")
action = input("> ")
        
if action == "add" or action == "subtract" or action == "multiply" or action == "divide":
    num2 = float(input("\nEnter your second number . . . "))

print("")

if action == "add":
    result = num1 + num2

elif action == "subtract":
    result = num1 - num2

elif action == "multiply":
    result = num1 * num2

elif action == "divide":
    result = num1 / num2

elif action == "square":
    result = num1 ** 2

elif action == "cube":
    result = num1 ** 3

elif action == "square root":
    result = math.sqrt(num1)

elif action == "cube root":
    result = numpy.cbrt(num1)

print("Result = ", result)
